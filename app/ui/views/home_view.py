class HomeView(Gtk.ScrolledWindow):
    def __init__(self) -> None:
        super().__init__()

        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.set_hexpand(True)
        self.set_vexpand(True)

        content = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        content.set_margin_top(24)
        content.set_margin_bottom(24)
        content.set_margin_start(24)
        content.set_margin_end(24)
        content.set_hexpand(True)
        content.set_vexpand(False)

        title = Gtk.Label(label="Home")
        title.add_css_class("title-1")
        title.set_halign(Gtk.Align.START)
        title.set_xalign(0)
        title.set_wrap(True)
        content.append(title)

        perf = self._safe_get_performance_metrics()
        storage = self._safe_get_storage_metrics()
        battery = self._safe_get_battery_status()
        power = self._safe_get_power_profile()

        perf_msg = self._safe_describe_performance(perf)
        storage_msg = self._safe_describe_storage(storage)

        score = self._calculate_score(
            self._safe_float(perf.get("cpu_percent")),
            self._safe_float(perf.get("ram_percent")),
            self._safe_float(storage.get("disk_percent")),
        )

        status_body = (
            f"Good · {score}/100\n\n"
            f"{perf_msg}\n"
            f"{storage_msg}\n\n"
            "ZorHUB pα0.2.1-dev only reads basic system information. "
            "It does not modify your system."
        )
        content.append(StatusCard("System status", status_body))

        grid = Gtk.Grid(column_spacing=12, row_spacing=12)
        grid.set_hexpand(True)
        grid.set_column_homogeneous(True)

        cpu_value = self._format_percent(perf.get("cpu_percent"))
        ram_value = self._format_percent(perf.get("ram_percent"))
        ram_subtitle = self._format_ram_subtitle(perf)
        storage_value = self._format_percent(storage.get("disk_percent"))
        storage_subtitle = self._format_storage_subtitle(storage)
        battery_text = self._format_battery_text(battery)

        grid.attach(MetricCard("CPU", cpu_value), 0, 0, 1, 1)

        grid.attach(
            MetricCard(
                "RAM",
                ram_value,
                ram_subtitle,
            ),
            1,
            0,
            1,
            1,
        )

        grid.attach(
            MetricCard(
                "Storage",
                storage_value,
                storage_subtitle,
            ),
            0,
            1,
            1,
            1,
        )

        grid.attach(
            MetricCard(
                "Battery",
                battery_text,
                "Battery information may not be available on all devices.",
            ),
            1,
            1,
            1,
            1,
        )

        content.append(grid)

        energy_profile = self._format_power_profile(power)

        content.append(
            StatusCard(
                "Energy mode",
                energy_profile,
            )
        )

        content.append(
            StatusCard(
                "ZorHUB Agent",
                (
                    "Not implemented in pα0.2.1-dev.\n\n"
                    "Advanced actions are disabled. ZorHUB Agent will be introduced "
                    "in a later pre-alpha stage and must not be installed or simulated "
                    "as a real system component in this version."
                ),
            )
        )

        self.set_child(content)

    def _safe_get_performance_metrics(self) -> dict:
        try:
            return get_performance_metrics()
        except Exception:
            return {
                "cpu_percent": None,
                "ram_percent": None,
                "ram_used_gb": None,
                "ram_total_gb": None,
                "swap_percent": None,
                "process_count": None,
            }

    def _safe_get_storage_metrics(self) -> dict:
        try:
            return get_storage_metrics()
        except Exception:
            return {
                "disk_percent": None,
                "disk_used_gb": None,
                "disk_free_gb": None,
                "disk_total_gb": None,
            }

    def _safe_get_battery_status(self) -> dict:
        try:
            return get_battery_status()
        except Exception:
            return {
                "available": False,
                "percent": None,
                "status": "Not available",
            }

    def _safe_get_power_profile(self) -> dict:
        try:
            return get_power_profile()
        except Exception:
            return {
                "available": False,
                "profile": "Not available",
            }

    def _safe_describe_performance(self, metrics: dict) -> str:
        try:
            _status, message = describe_performance(metrics)
            return message
        except Exception:
            return "Performance information is partially unavailable."

    def _safe_describe_storage(self, metrics: dict) -> str:
        try:
            _status, message = describe_storage(metrics)
            return message
        except Exception:
            return "Storage information is partially unavailable."

    def _safe_float(self, value) -> float:
        try:
            if value is None:
                return 0.0
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    def _format_percent(self, value) -> str:
        if value is None:
            return "Not available"

        try:
            return f"{float(value):.1f}%"
        except (TypeError, ValueError):
            return "Not available"

    def _format_ram_subtitle(self, metrics: dict) -> str:
        used = metrics.get("ram_used_gb")
        total = metrics.get("ram_total_gb")

        if used is None or total is None:
            return "Memory details are not available."

        return f"{used} GB / {total} GB"

    def _format_storage_subtitle(self, metrics: dict) -> str:
        free = metrics.get("disk_free_gb")
        total = metrics.get("disk_total_gb")

        if free is None:
            return "Storage details are not available."

        if total is None:
            return f"{free} GB free"

        return f"{free} GB free / {total} GB total"

    def _format_battery_text(self, battery: dict) -> str:
        if not battery.get("available"):
            return "Not available"

        percent = battery.get("percent")
        status = battery.get("status", "Unknown")

        if percent is None:
            return f"Unknown · {status}"

        return f"{percent}% · {status}"

    def _format_power_profile(self, power: dict) -> str:
        profile = power.get("profile")

        if not profile or profile == "Not available":
            return (
                "Not available.\n\n"
                "Power profile information could not be detected. This may happen if "
                "`power-profiles-daemon` is not installed, not active, or not supported "
                "by this system."
            )

        return (
            f"{profile}\n\n"
            "This is read-only in pα0.2.1-dev. ZorHUB does not change the system "
            "energy profile in this version."
        )


    # will be deleted in pa0.3 or pa0.4
    def _calculate_score(self, cpu: float, ram: float, disk: float) -> int:
        score = 100

        if cpu > 70:
            score -= 10
        if cpu > 90:
            score -= 15

        if ram > 80:
            score -= 10
        if ram > 90:
            score -= 15

        if disk > 80:
            score -= 10
        if disk > 90:
            score -= 15

        return max(score, 0)

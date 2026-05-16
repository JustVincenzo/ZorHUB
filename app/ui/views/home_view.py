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

        perf = get_performance_metrics()
        storage = get_storage_metrics()
        battery = get_battery_status()
        power = get_power_profile()

        _perf_status, perf_msg = describe_performance(perf)
        _storage_status, storage_msg = describe_storage(storage)

        score = self._calculate_score(
            float(perf["cpu_percent"]),
            float(perf["ram_percent"]),
            float(storage["disk_percent"]),
        )

        status_body = f"Good · {score}/100\n\n{perf_msg}\n{storage_msg}"
        content.append(StatusCard("System status", status_body))

        grid = Gtk.Grid(column_spacing=12, row_spacing=12)
        grid.set_hexpand(True)
        grid.set_column_homogeneous(True)

        grid.attach(MetricCard("CPU", f"{perf['cpu_percent']}%"), 0, 0, 1, 1)
        grid.attach(
            MetricCard(
                "RAM",
                f"{perf['ram_percent']}%",
                f"{perf['ram_used_gb']} GB / {perf['ram_total_gb']} GB",
            ),
            1,
            0,
            1,
            1,
        )
        grid.attach(
            MetricCard(
                "Storage",
                f"{storage['disk_percent']}%",
                f"{storage['disk_free_gb']} GB free",
            ),
            0,
            1,
            1,
            1,
        )

        battery_text = (
            "Not available"
            if not battery.get("available")
            else f"{battery['percent']}% · {battery['status']}"
        )
        grid.attach(MetricCard("Battery", battery_text), 1, 1, 1, 1)

        content.append(grid)

        content.append(StatusCard("Energy mode", str(power.get("profile", "Not available"))))
        content.append(
            StatusCard(
                "ZorHUB Agent",
                "Not installed. Advanced actions are disabled in this private pre-alpha.",
            )
        )

        self.set_child(content)

# ZorHUB

**ZorHUB** is a visual, friendly, and secure hub for [Linux](https:/linux.org/)/[Zorin OS](https://zorin.com/os/) focused on system care, metrics, safe actions, customization, application management, device integration, and future extensions.

The project is designed primarily for [Zorin OS](https://zorin.com/os/) and Ubuntu-based [Linux](https:/linux.org/) distributions, with possible support for more [Linux](https:/linux.org/) distributions in the future.

ZorHUB is inspired by the user experience philosophy of tools like Samsung Device Care: clear status, simple language, visible metrics, and guided actions. ZorHUB is not intended to be just another technical system monitor. Its goal is to make [Linux](https:/linux.org/) processes more understandable, safer to control, and easier to access.

> ZorHUB is an independent project and is not affiliated with, endorsed by, or maintained by [Zorin OS](https://zorin.com/os/) Technologies Ltd., Samsung, GNOME, KDE, or any other referenced company or project.

## Project status

ZorHUB is currently in early development.

Current target:

```text
ZorHUB pα0.2
- Local desktop prototype
- Main dashboard
- System status score
- CPU, RAM, disk, and battery metrics
- Human-readable language and recommendations
- Basic energy profile interface
```

Future target:

```text
ZorHUB Main
- Distributed as Flatpak
- Friendly visual interface
- Metrics and system care
- Extension support
- Application management experience
- Device integration modules
- Simple and advanced user modes

ZorHUB Helper
- Native system component
- Installed separately
- Provides privileged system actions
- Uses a safer permission model
- Communicates with ZorHUB Main
```

## Core idea

ZorHUB is designed to be more than a system monitor.

It is a **hub**: a central environment where system care, metrics, safe actions, diagnostics, customization, application management, device integration, and future extensions can work together through a simple and visual interface.

The main idea is:

```text
Human status + clear metric + short explanation + safe action
```

Instead of showing only raw technical data like:

```text
RAM: 82%
CPU: 46%
Disk: 88%
```

ZorHUB should explain what those numbers mean:

```text
Memory usage is high: 82%

Your system is using a high amount of RAM.
This may slow down the computer if more applications are opened.

Recommended action:
Review high-consumption applications.
```

ZorHUB should not hide technical information. It should organize it better.

The user should first see a clear and human-readable summary, and then be able to open advanced technical details if needed.

ZorHUB does not replace [Linux](https:/linux.org/) tools. It unifies, explains, and safely controls them.

## Why ZorHUB exists

[Linux](https:/linux.org/) is powerful, but many common tasks are fragmented across different tools, package formats, settings panels, terminal commands, and background services.

On [Zorin OS](https://zorin.com/os/) and Ubuntu-based systems, users may interact with:

```text
APT packages
Flatpak applications
Snap packages
AppImages
External .deb installers
System settings
Terminal commands
System services
Device integration tools
Update managers
Software stores
Flatpak permissions
```

For experienced users, this flexibility is useful. For regular users, it can become confusing.

ZorHUB exists to reduce that fragmentation.

Its goal is to provide a central, friendly, and safe environment where users can understand what is happening, choose recommended actions, and access system features without needing to manually navigate multiple disconnected tools.

ZorHUB does not try to remove the power of [Linux](https:/linux.org/). It tries to organize it.

## Purpose

The purpose of ZorHUB is to make [Linux](https:/linux.org/) system management more understandable, visual, and safe.

[Linux](https:/linux.org/) gives users powerful tools, but many of them are fragmented, technical, or terminal-based. ZorHUB aims to create a familiar environment where users can understand what is happening on their system and take safe actions without manually executing commands.

ZorHUB is designed for users who want:

- A clear view of their system status.
- Visible but understandable metrics.
- Human-readable recommendations.
- Safe actions instead of raw terminal commands.
- A friendlier way to install and manage applications.
- A central place for system care and diagnostics.
- Integration with tools such as Zorin Connect.
- Customization without unnecessary complexity.
- Future official and community-made extensions.

ZorHUB does not try to replace system tools. It tries to make them easier to understand, safer to use, and better connected.

## Visual philosophy

ZorHUB should be friendly, clean, and familiar.

The interface should be inspired by modern system care tools, while keeping useful [Linux](https:/linux.org/) metrics available.

The visual design should prioritize:

```text
Status first.
Metrics second.
Explanation third.
Action last.
```

Each section should answer a human question:

| User question | ZorHUB section |
|---|---|
| Is my system okay? | Home |
| Why is my computer slow? | Performance |
| Why is my storage almost full? | Storage |
| What can I safely do? | Care |
| What is consuming resources? | Applications |
| How do I install this app properly? | App Hub |
| Is my phone connected? | Devices |
| What happened before? | History |
| What can I customize? | Settings |
| What can I add? | Extensions |

ZorHUB should provide two levels of information:

```text
Simple mode:
- Human-readable status
- Main metrics
- Recommended actions

Advanced mode:
- Detailed metrics
- Technical information
- Logs
- System-level explanations
```

ZorHUB should be friendly, but not childish. Technical, but not overwhelming.

## ZorHUB Main

**ZorHUB Main** is the main graphical application.

It is responsible for:

- Showing the user interface.
- Displaying system status.
- Showing metrics such as CPU, RAM, disk, and battery usage.
- Giving human-readable recommendations.
- Managing user preferences.
- Loading future extensions.
- Providing access to system care modules.
- Providing access to App Hub and device integration modules.
- Communicating with ZorHUB Helper when advanced system actions are needed.

ZorHUB Main is planned to be distributed as a **Flatpak** application.

This keeps the main app easier to install, update, and isolate from the base system.

However, because Flatpak applications are sandboxed, some advanced system actions cannot be performed directly from ZorHUB Main. That is why ZorHUB Helper is planned as a separate component.

## ZorHUB Helper

**ZorHUB Helper** is a future native system component used for advanced and privileged actions.

It is not the main app. It is an optional system extension that allows ZorHUB Main to request deeper system operations in a controlled way.

ZorHUB Helper may be used for actions such as:

- Checking system package updates.
- Installing applications through supported package managers.
- Repairing package manager issues.
- Managing system services.
- Performing advanced cleanup tasks.
- Changing system-level settings.
- Running diagnostics that require deeper access.

ZorHUB Helper should be installed separately from ZorHUB Main.

The expected flow is:

```text
1. User installs ZorHUB Main.
2. User opens ZorHUB.
3. ZorHUB detects that Helper is not installed.
4. ZorHUB explains what Helper does.
5. User chooses whether to install it.
6. Helper is installed separately.
7. ZorHUB Main and ZorHUB Helper communicate securely.
8. Advanced actions become available.
```

ZorHUB Main must still work without ZorHUB Helper.

Without Helper, ZorHUB should provide basic metrics, visual status, non-privileged checks, and interface features. With Helper installed, ZorHUB can unlock deeper system care, app installation, and system management features.

## App Hub

ZorHUB plans to include an application management experience called **App Hub**.

App Hub is not intended to be only a traditional software store. Its purpose is to help users understand and choose between different installation sources in a clearer way.

[Linux](https:/linux.org/) applications may be available through different formats, such as:

```text
APT / DEB
Flatpak
Snap
AppImage
External .deb packages
```

Instead of exposing these options without context, App Hub should explain the differences and recommend the most suitable option when possible.

Example:

```text
Application: Spotify

Available sources:
- APT/DEB: better system integration
- Flatpak: more isolated, may use more storage
- Snap: available, but may behave differently

Recommended option:
APT/DEB
```

App Hub should prioritize:

- Clear source comparison.
- Human-readable explanations.
- Safe installation actions.
- Technical details for advanced users.
- No arbitrary command execution.
- Verification when installing external packages.

Privileged installation actions may require ZorHUB Helper.

## Zorin Connect visual integration

ZorHUB plans to integrate [**Zorin Connect**](https://zorin.com/os/#:~:text=Your%20phone%20and%20computer%20work,.) directly into its visual interface.

The goal is not to replace Zorin Connect, duplicate its features, or create a separate device connection app. Instead, ZorHUB should act as a clearer and more centralized visual layer for Zorin Connect inside the hub experience.

Zorin Connect would remain the underlying tool responsible for phone-to-computer communication. ZorHUB would provide a friendlier interface to display its status, expose useful actions, and make device integration easier to understand.

Possible visual features inside ZorHUB:

```text
Connected phone status
Phone battery level
Connection state
Send files
Send links
Find phone
Open Zorin Connect settings
Connection diagnostics
Quick device actions
```
This means ZorHUB would not be a replacement for Zorin Connect. It would be a visual hub layer that makes Zorin Connect easier to access, understand, and use from one central place.

## License

This project is licensed under the GNU General Public License v3.0.

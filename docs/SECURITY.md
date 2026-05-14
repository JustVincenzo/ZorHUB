# Security Policy

ZorHUB is designed to provide safe and guided access to Linux system actions.

Some ZorHUB features may require privileged permissions, especially actions related to package management, system services, advanced cleanup, network configuration, or system-level diagnostics.

However, ZorHUB should not execute arbitrary commands directly and should not run the entire graphical application as root.

## Security principles

ZorHUB should follow these principles:

- Do not run the main graphical application as root.
- Do not expose arbitrary command execution to the user.
- Do not execute raw user-provided shell commands.
- Do not hide privileged actions from the user.
- Do not modify system-level settings without explanation.
- Do not install, remove, or repair packages without user confirmation.
- Do not perform high-risk actions without system authorization.

Privileged actions must be explicit, limited, explained, and authorized.

## Privileged actions

ZorHUB may support privileged actions in the future.

Examples:

- Installing applications.
- Removing applications.
- Checking package updates.
- Repairing package manager issues.
- Managing system services.
- Restarting selected services.
- Changing system-level settings.
- Running advanced diagnostics.
- Performing advanced cleanup tasks.

These actions should require system authorization.

On Linux, this may be handled through tools such as Polkit/pkexec or a dedicated ZorHUB Helper component.

## Authorization model

ZorHUB should not simply run commands with `sudo` from the graphical interface.

Instead, privileged actions should follow this model:

```text
1. User requests an action from ZorHUB Main.
2. ZorHUB explains what the action will do.
3. ZorHUB shows the risk level.
4. User confirms the action.
5. ZorHUB requests system authorization.
6. The system displays an authentication prompt.
7. If authorized, the action is executed.
8. ZorHUB shows the result.
9. The action is recorded in the history/log.
```

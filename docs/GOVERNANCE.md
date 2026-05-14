# Governance

ZorHUB is maintained as an official project by its original author and maintainer.

This document defines how the official ZorHUB project is managed, how contributions are reviewed, how forks are treated, and how official extensions are approved.


## Official project

The official ZorHUB repository is:

```text
https://github.com/Vynzaro/ZorHUB
```

Only the code, releases, documentation, and packages published through the official repository or other maintainer-approved channels are considered official ZorHUB material.

Forks, modified versions, third-party builds, and redistributed packages are not official unless explicitly approved by the maintainer.


## Maintainer

The original author and maintainer of ZorHUB is:

```text
Vinxenzzo / Vynzaro
```

The maintainer is responsible for:

- Defining the project vision.
- Maintaining the official repository.
- Reviewing pull requests.
- Accepting or rejecting contributions.
- Approving official releases.
- Approving official extensions.
- Defining the safety model.
- Protecting the official identity of ZorHUB.
- Deciding the technical direction of the project.

The maintainer has final decision-making authority over the official ZorHUB project.


## Project vision

ZorHUB is a visual and secure hub for Linux/Zorin OS that aims to unify fragmented system tasks through a friendly interface.

The project focuses on:

- System care.
- Clear metrics.
- Human-readable explanations.
- Safe actions.
- Application management.
- Zorin Connect visual integration.
- Customization.
- Extensions.
- Linux/Zorin OS integration.

Contributions should respect this direction.

A contribution may be rejected if it does not fit the project vision, even if it works technically.


## Official codebase

The official ZorHUB codebase is the code maintained in the official repository.

Changes to the official codebase may only be accepted through maintainer review and approval.

No external contributor has the right to directly modify the official codebase without permission.

The `main` branch should be treated as the stable official development branch.

Direct changes to `main` should be restricted to the maintainer or approved maintainers.


## Branch policy

The official repository should use a protected branch model.

Recommended branch structure:

```text
main
├── Official stable development branch
│
dev
├── Optional active development branch
│
feature/*
├── Feature branches
│
fix/*
├── Bug fix branches
│
docs/*
└── Documentation branches
```

Recommended GitHub branch protection for `main`:

- Require pull requests before merging.
- Require maintainer approval.
- Block force pushes.
- Block branch deletion.
- Require conversation resolution before merging.
- Require status checks when automated tests are added.


## Contributions

External contributions are welcome, but they are not automatically accepted.

Contributions should be submitted through pull requests.

A pull request may be:

- Accepted.
- Rejected.
- Closed without merge.
- Sent back for changes.
- Delayed if it does not fit the current roadmap.
- Reworked by the maintainer before merge.

Submitting a pull request does not guarantee inclusion in the official project.


### Pull request requirements

Pull requests should clearly explain:

- What was changed.
- Why the change is needed.
- What problem it solves.
- Whether it affects security.
- Whether it affects privileged actions.
- Whether it changes the user interface.
- Whether it changes documentation.
- Whether it introduces new dependencies.

Pull requests that affect privileged actions, package installation, system services, external downloads, extensions, or command execution require stricter review.


### Contribution standards

Accepted contributions should follow these standards:

- Keep the code readable.
- Keep the architecture modular.
- Avoid large single-file implementations.
- Avoid unnecessary dependencies.
- Avoid arbitrary command execution.
- Avoid unsafe privileged behavior.
- Respect the safety model.
- Respect the visual philosophy.
- Respect Linux/Zorin OS conventions.
- Explain technical behavior clearly to users.

Contributions that make ZorHUB harder to understand, less safe, or less aligned with the project vision may be rejected.


## Safety-first rule

ZorHUB may interact with sensitive parts of the system.

Because of this, safety is a core governance rule.

The official project must not accept changes that:

- Execute arbitrary user-provided shell commands.
- Run the entire graphical application as root.
- Hide privileged actions from users.
- Install external packages without verification.
- Modify system configuration without explanation.
- Bypass the ZorHUB Helper safety model.
- Bypass user confirmation for high-risk actions.
- Misrepresent risky actions as harmless.

Privileged actions must be declared, limited, explained, and authorized.


## Forks

Forks are allowed under the terms of the project license.

A fork may:

- Modify ZorHUB.
- Experiment with new features.
- Create alternative builds.
- Propose changes through pull requests.
- Develop unofficial extensions.
- Distribute modified versions if the license terms are respected.

However, forks are not official ZorHUB releases unless explicitly approved by the maintainer.

Forks must not claim to be the original or official ZorHUB project.


## Modified versions

Modified versions of ZorHUB must clearly state that they are modified.

They must not be distributed in a way that confuses users into believing they are using the official ZorHUB release.

Recommended wording for modified versions:

```text
This is an unofficial modified version of ZorHUB.
It is not maintained, reviewed, or approved by the original ZorHUB maintainer.
```

Modified versions should use a clear label or distinguishable name when distributed publicly.

Examples:

```text
ZorHUB Community Build
ZorHUB Experimental Build
ZorHUB Fork by <author>
```

The name must not imply official approval unless such approval was granted by the maintainer.

## Official releases

Only the maintainer may publish official ZorHUB releases.

Official releases may include:

- Source code archives.
- Flatpak builds.
- Helper packages.
- Documentation releases.
- Approved extension packages.
- Release notes.

A release is official only if it is published through the official repository or another maintainer-approved channel.

Unofficial builds, third-party packages, forks, and redistributed versions are not official releases.


## ZorHUB Helper governance

ZorHUB Helper is planned as a separate native system component for privileged actions.

Because it may interact with package managers, system services, permissions, diagnostics, and system-level operations, it requires stricter governance.

Changes to ZorHUB Helper must be reviewed with special attention to:

- Privileged execution.
- Authorization model.
- Polkit/pkexec usage.
- Package manager behavior.
- System service management.
- External downloads.
- Logging.
- User confirmation.
- Error handling.
- Rollback or recovery behavior.

Unsafe Helper changes should not be merged.


## Extension governance

ZorHUB may support extensions in the future.

Extensions are intended to expand ZorHUB without modifying the core code directly.

Possible extension types:

```text
Visual extensions
Integration extensions
Action extensions
Diagnostic extensions
```

Extensions may be created by the community, but they are not official unless reviewed and approved by the maintainer.


## Official extensions

An official extension is an extension that has been reviewed, approved, and listed by the maintainer.

Official extensions must:

- Follow the ZorHUB safety model.
- Declare their purpose clearly.
- Declare required permissions.
- Avoid arbitrary command execution.
- Avoid unnecessary system access.
- Respect the user’s system appearance when possible.
- Provide clear user-facing explanations.
- Avoid misleading branding.
- Be maintainable.

Official extensions may be distributed through official ZorHUB channels.


## Community extensions

Community extensions are allowed.

However, community extensions are not official by default.

Community extensions must not claim to be official unless approved by the maintainer.

Recommended wording:

```text
This is a community extension for ZorHUB.
It is not an official ZorHUB extension unless approved by the maintainer.
```

Community extensions should clearly state:

- Author.
- Purpose.
- Required permissions.
- Supported ZorHUB version.
- Whether ZorHUB Helper is required.
- Whether the extension performs privileged actions.


## Extension approval

To be approved as official or trusted, an extension should be reviewed for:

- Security.
- Stability.
- Code quality.
- User experience.
- Permission usage.
- Compatibility with ZorHUB’s design.
- Compliance with the safety model.
- Compliance with the project vision.

The maintainer may reject an extension if it is unsafe, unclear, unnecessary, misleading, poorly maintained, or inconsistent with ZorHUB’s goals.


## Branding and official identity

The name “ZorHUB” identifies the official project.

Forks, modified versions, third-party packages, and community extensions must not use the ZorHUB name in a misleading way.

Allowed usage:

```text
Fork of ZorHUB
Unofficial build of ZorHUB
Extension for ZorHUB
Compatible with ZorHUB
```

Not allowed:

```text
Official ZorHUB
Original ZorHUB
ZorHUB Stable Release
Approved ZorHUB Build
```

unless explicitly approved by the maintainer.

The goal is not to prevent forks. The goal is to prevent confusion.


## Documentation governance

Documentation changes should follow the same principles as code changes.

Documentation should be:

- Clear.
- Accurate.
- Honest about limitations.
- Consistent with the project vision.
- Consistent with the security model.
- Understandable for regular users.
- Useful for advanced users when needed.

Documentation must not promise features that do not exist unless they are clearly marked as planned.


## Roadmap governance

The roadmap is controlled by the maintainer.

Community suggestions are welcome, but roadmap inclusion is not guaranteed.

A feature may be delayed or rejected if it:

- Adds unnecessary complexity.
- Creates security risk.
- Breaks the visual philosophy.
- Does not fit the hub concept.
- Requires unstable dependencies.
- Duplicates existing tools without improving the experience.
- Makes ZorHUB feel like a terminal wrapper instead of a guided hub.


## Decision-making model

ZorHUB uses a maintainer-led governance model.

This means:

```text
Discussion is welcome.
Contributions are welcome.
Forks are allowed.
Pull requests are reviewed.
Final decisions belong to the maintainer.
```

This model exists to protect the consistency, safety, and identity of the official project.


## Conflict resolution

If there is disagreement about a change, the maintainer may decide based on:

- Project vision.
- User safety.
- Technical quality.
- Maintainability.
- Long-term direction.
- Compatibility with the safety model.
- Compatibility with the official design philosophy.

The maintainer may close discussions or pull requests that become unproductive, unsafe, abusive, or unrelated to the project.


## Inactive contributions

Pull requests or issues may be closed if they become inactive for a long period.

A contribution may be considered inactive if:

- Requested changes are not addressed.
- The code no longer applies cleanly.
- The proposal no longer fits the roadmap.
- The contributor does not respond.
- The project architecture has changed.

Closed contributions may be reopened or resubmitted later if they become relevant again.


## Maintainer rights

The maintainer reserves the right to:

- Accept or reject contributions.
- Edit submitted contributions before merging.
- Reorganize code.
- Change roadmap priorities.
- Change project structure.
- Rename planned modules.
- Remove unsafe features.
- Reject features that do not fit the project vision.
- Approve or reject official extensions.
- Decide what is considered an official ZorHUB release.

These rights apply only to the official ZorHUB project and do not prevent forks allowed under the project license.


## License relationship

This governance document does not replace the project license.

The project license defines the legal rights to use, copy, modify, and distribute ZorHUB.

This governance document defines what is considered official within the ZorHUB project.

In simple terms:

```text
The license controls what people may legally do with the code.
Governance controls what becomes part of the official project.
```

Forks and modified versions may exist under the license, but they are not official unless approved by the maintainer.

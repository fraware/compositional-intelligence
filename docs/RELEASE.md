# Publication protocol

This repository is **public**. Every committed branch and draft pull request is publicly readable. GitHub's noindex settings do not restrict access to files, and deleting a file from a later commit does not revoke access to earlier commits.

## Current permitted content

Only public-safe website styling, configuration, tests, and release documentation are eligible for this repository. The canonical Version 7 website contains nine full-text reading pages and must remain outside the repository pending the author's explicit publication decision. Never copy sources/, editorial/, qa/, site/essays/, or unapproved site/index.html into a public branch.

## Release conditions

Before a public content commit, complete all of the following independently:

1. Author approve the public edition of the synthesis, preface, and each companion essay.
2. Adjudicate the mathematical-definition, notation, and scientific-claim reviews.
3. Verify the bibliography and every citation-to-claim relationship.
4. Approve copyright, redistribution rights, attribution, affiliation, publication date, and canonical domain.
5. Run full-text fidelity, link, accessibility, responsive, and staging-host browser checks.
6. Remove private editorial and provenance artifacts from the deployable build.
7. Review the exact Git tree and commit history for confidential manuscript content before changing the content allowlist.
8. Only then approve public deployment and search indexing.

## Operational safeguards

Run python3 tools/check_public_tree.py on the working Git checkout. The current allowlist intentionally refuses HTML reading pages and manuscript files. It is a preflight check, not a GitHub permission control, and its rules must be updated only as part of an explicitly approved public release.

The existing Version 7 site-builder release checks are retained in the private research package. GitHub Actions and GitHub Pages are intentionally unconfigured. In particular, billing constraints should not be bypassed by weakening release safeguards.

For staging prior to publication, use a **private** repository or access-controlled artifact store; a branch of this repository is not private staging.

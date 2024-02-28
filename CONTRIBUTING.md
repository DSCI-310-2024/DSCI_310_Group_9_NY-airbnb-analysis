# Contributing to Airbnb Analysis

Thank you for considering contributing to our Airbnb Analysis project! This project aims to provide in-depth insights and analysis of Airbnb listings, helping both hosts and guests make informed decisions. We welcome contributions from everyone, including data analysis, code enhancements, documentation improvements, and example notebooks.

## How to Contribute

### Issues and Discussions

- **Bugs & Issues**: If you encounter a bug or issue with our analysis or code, please open an issue on our [GitHub Repository](https://github.com/DSCI-310-2024/DSCI_310_Group_9_NY-airbnb-analysis). Please provide as much detail as possible to help us understand and address the issue efficiently.

- **Feature Requests & Suggestions**: We're always looking for new ideas and improvements! Feel free to submit feature requests or suggestions through the GitHub issues.

- **Questions & Discussions**: Have questions or want to discuss ideas? Start a conversation in the GitHub Discussions section of our repository.

### Code Contributions

If you're looking to contribute code, here's how you can do it:

#### Setting Up Your Environment

1. Fork the Airbnb Analysis repository on GitHub.
2. Clone your fork locally:
    ```bash
    git clone https://github.com/DSCI-310-2024/DSCI_310_Group_9_NY-airbnb-analysis
    ```
3. Set up your development environment using the provided `dsci.yml` file. This will ensure you have all the necessary dependencies installed:
    ```bash
    conda env create -f dsci.yml
    conda activate dsci
    ```
4. Keep your fork up to date with the main repository by setting up an upstream remote:
    ```bash
    git remote add upstream https://github.com/DSCI-310-2024/DSCI_310_Group_9_NY-airbnb-analysis
    git fetch upstream
    git checkout main
    git merge upstream/main
    ```

#### Making Changes

1. Create a new branch for your changes:
    ```bash
    git checkout -b your-branch-name
    ```
2. Make your changes, add new features, or fix bugs.
3. If you're adding new analysis or data, ensure it adheres to our data handling and privacy standards.
4. Test your changes thoroughly.

#### Submitting Your Contribution

1. Commit your changes with a meaningful commit message.
2. Push your changes to your fork:
    ```bash
    git push origin your-branch-name
    ```
3. Open a pull request (PR) against the main repository. Ensure you describe your changes or additions in detail.

### Documentation Contributions

We value documentation just as much as code. You can contribute by:

- **Improving Documentation**: Clarify existing documentation, add examples, or create new sections to help others understand the project better.
- **Writing Tutorials or Examples**: Share your knowledge and experiences with the project by adding new tutorials or example notebooks.

### Review Process

All contributions will be reviewed by project maintainers. We aim to provide feedback and guidance as necessary to ensure high-quality and consistent contributions. Once approved, your contributions will be merged into the project.

## Code of Conduct

We are committed to providing a welcoming and inclusive environment for all. By participating in this project, you agree to abide by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## Questions?

If you have any questions or need further guidance on contributing, please reach out to us via GitHub issues or discussions.

---

Thank you for contributing to the Airbnb Analysis project! Your efforts help make this project more valuable for everyone.

---

This contribution guide is part of our Airbnb Analysis project. Made with ❤️ by the Airbnb Analysis team. Licensed under the [CC0](./LICENSE).
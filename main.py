from importlib import import_module


def main():
    packages = (
        "sklearn", "pandas", "numpy", "matplotlib",
        "seaborn", "shap", "jupyterlab", "joblib", "scipy",
    )
    for package in packages:
        import_module(package)
    print("Ambiente OK.")


if __name__ == "__main__":
    main()

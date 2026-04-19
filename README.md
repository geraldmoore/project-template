# Project Template

A [Copier](https://copier.readthedocs.io/) template for Python projects using [uv](https://docs.astral.sh/uv/) and [prek](https://prek.j178.dev/) for git hook management.

## Prerequisites

- [copier](https://copier.readthedocs.io/)
- [copier-template-extensions](https://github.com/copier-org/copier-template-extensions)
- [python-slugify](https://github.com/un33k/python-slugify)

```bash
pip install copier
pip install copier-template-extensions
pip install python-slugify
```

## Usage

### Generate a new project

```bash
copier copy --trust gh:geraldmoore/project-template /path/to/your/project
```

During project generation, you will be prompted to configure:

**General Options:**
- Project name, description, author details
- Python version and CI versions
- License (MIT, Apache-2.0, GPL-3.0)
- Pydantic settings setup
- Logging setup

**ML Options (if building an ML project):**
- ML framework: PyTorch, TensorFlow, or framework-agnostic
- Experiment tracking: Weights & Biases, MLflow, or none

### Git initialise the new project

Change directory to yor new project then initialise `git`:

```bash
git init
```

### Update an existing project

In the project repository:

```bash
copier update
```

## ML Project Features

When creating an ML project, the template includes:

**Structure:**
```
src/{{ module_name }}/
├── ml/
│   ├── configs/      # Pydantic config schemas (model, training, data, experiment)
│   ├── data/         # Data loading and transforms
│   ├── models/       # Model architectures (base, MLP example)
│   ├── tracking/     # Experiment tracking (W&B or MLflow)
│   ├── train.py      # Training pipeline
│   ├── evaluate.py   # Evaluation pipeline
│   └── predict.py    # Inference pipeline
configs/
├── default_config.yaml      # Default experiment config
└── experiment_example.yaml  # Example custom config
```

**Configuration:**
- YAML configs validated through pydantic
- Separate configs for model, training, data, and experiment settings
- Load configs via `ExperimentConfig.from_yaml("path/to/config.yaml")`

**Experiment Tracking:**
- **Weights & Biases**: Metrics, params, model artifacts, gradient watching
- **MLflow**: Metrics, params, model registry support
- Both trackers share a common interface for easy switching

**Pipeline:**
- `train()`: Full training loop with checkpointing, early stopping, LR scheduling
- `evaluate()`: Test set evaluation with metrics computation
- `predict()`: Single and batch inference

## Main Template README for more details

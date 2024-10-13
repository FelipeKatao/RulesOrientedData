# DataDrivenRulesEngine

## Overview
DataDrivenRulesEngine is a flexible and dynamic rule processing engine designed to evaluate business logic based on rules defined in JSON format. This project allows users to define complex conditions and actions without hardcoding them into the application, promoting modularity and maintainability.

## Features
- **Dynamic Rule Processing**: Process rules defined in JSON files, enabling easy updates without changing the codebase.
- **Custom Conditions**: Evaluate custom conditions using both integer and string comparisons.
- **Sub-rule Execution**: Support for executing additional rules based on defined actions, enhancing rule interdependencies.
- **Logging Mechanism**: Track the flow of rule evaluations and the values used in the process for easier troubleshooting.

## Getting Started
To get started with DataDrivenRulesEngine, clone the repository and install the required dependencies.

```bash
git clone https://github.com/yourusername/DataDrivenRulesEngine.git
cd DataDrivenRulesEngine
```
## Requirements
Python 3.x
JSON files for rule definitions


#Usage
To use the rules engine, instantiate the OrientionData class and call the ProcessRulesOd method with the desired parameters.

Python
```python

from OrientionData import OrientionData

od = OrientionData()
result = od.ProcessRulesOd(your_rule_definition, value1, value2)
```
JavaScript 
```JavaScript

```

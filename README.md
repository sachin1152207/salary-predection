
# Salary Predection

This is simple salary predector code in python using sklearn. The algorithims is used in this code is ExtraTreesRegressor. with some hypertunning parameters


## Run Locally

Clone the project

```bash
  git clone https://github.com/sachin1152207/salary-predection
```

Go to the project directory

```bash
  cd salary-predection
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python __init__.py
```


## API Reference

#### Get predection

```http
  GET /api/predict
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `educ` | `string` | **Required**.  Your education|
| `job` | `string` | **Required**.  Your job post|
| `exp` | `int` | **Required**.  Your experince year|
| `age` | `int` | **Required**.  Your age in year|
| `gender` | `int` | **Required**.  Male: 0, Female: 1, Other: 2|




## Authors

- [@sachin1152207](https://www.github.com/sachin1152207)



# Tonnumber API

QRCODE generator API


## API Reference

#### Generate QRcode

```http
  GET /api/v1/generate?data={data}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `data` | `string` | **Required**. Your Data |




## Run Locally

Clone the project

```bash
  git clone https://github.com/v3nus7/base_bot.git
```

Go to the project directory

```bash
  cd base_bot
```

Install dependencies

```bash
  pip install -r requirements.txt
```
To Run

```bash
  uvicorn app.main:app --reload
```

## Authors

- [@javadnr](https://github.com/javanr)
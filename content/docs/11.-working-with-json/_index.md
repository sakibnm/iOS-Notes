---
coverY: 0
---

# 11. Working with APIs and JSON

JSON stands for JavaScript Object Notation. It is a standard text-based format for representing structured data. It follows the JavaScript object syntax. It is the most popular standard of text data for web APIs nowadays. That means almost all the APIs you will work with or build will be structured in JSON. So it is paramount to learn how to parse JSON data and use them in iOS.

### JSON Structure

Since JSON is a string that resembles JavaScript object syntax, we can put all basic data types inside a JSON string - strings, numbers, arrays, booleans, etc.

### JSON Object

For example, a simple JSON string for a contact would be:

```json
{
    "name": "Alex F",
    "email": "alex@email.com",
    "phone": 1234567890
}
```

This JSON string is exactly like a JavaScript object having three attributes: `name`, `email`, and `phone`. Each attribute has its values (like key-value pairs). Notice that this object contains string type values for name and email and an integer type value for phone.

Another JSON object representing an address could be:

```json
{
    "line1": "100 Winter Street",
    "line2": "Apt 202",
    "city": "Boston",
    "state": "MA",
    "zip": 02115
}
```

Now, a contact that includes an address could be written as:

```json
{
    "name": "Alex F",
    "email": "alex@email.com",
    "phone": 1234567890,
    "address": {
        "line1": "100 Winter Street",
        "line2": "Apt 202",
        "city": "Boston",
        "state": "MA",
        "zip": 02115
    }
}
```

So we can create a hierarchy of objects in JSON. A JSON object can hold other JSON objects.

### JSON Array

JSON can hold arrays of JSON objects as well. As usual, we use `[]` to define an array of JSON objects. For example, we can define an array of contact JSON objects written above:

```json
{
    "contacts": [
        {
            "name": "Alex F",
            "email": "alex@email.com",
            "phone": 1234567890,
            "address": {
                "line1": "100 Winter Street",
                "line2": "Apt 202",
                "city": "Boston",
                "state": "MA",
                "zip": 02115
            }
        },

        {
            "name": "Bob P",
            "email": "bob@email.com",
            "phone": 9864567890,
            "address": {
                "line1": "100 Summer Street",
                "line2": "Apt 562",
                "city": "Boston",
                "state": "MA",
                "zip": 02115
            }
        },

        {
            "name": "Max V",
            "email": "max@email.com",
            "phone": 9123456790,
            "address": {
                "line1": "300 Summer Street",
                "line2": "Apt 582",
                "city": "Boston",
                "state": "MA",
                "zip": 02115
            }
        }
    ]
}
```

In this module, we will build a new app, App11, to demonstrate JSON data parsing.

App11 will look the same as App10, but we will use a JSON-based API.

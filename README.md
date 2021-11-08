
# Dumb DB

## Are you looking for a reliable database management system? 
Then you've come to the wrong place. 

This is a very small database management system to store a minuscule amount of data in one of the worst possible ways. But hey, atleast its easy to use .

## Installation

Installation is super easy. Just use your favorite package manager.

```bash
  pip install dumbdb
```
    
## Usage/Examples

```python
from dumbdb import DumbDB

my_db = DumbDB(location="/tmp", file_name="temp_data.json")

# Use .set to set value
my_db.set("int", 1)
my_db.set("list", [])
my_db.set("cars", {})

# Use .get to get value
my_db.get("int")

# You can optionally pass a default value to the get method

my_db.get("new_key", default="Default Val")

```


## Advantages and Disadvantages

A good DMBS is characterized by the following. You can have a look how well the module fits the ideal DMBS.


| Desired Feature | Module Status |
|---|---|
| Data Availability | Data is stored in a file in JSON format. Your operating system handles data availability, but it is only accessible locally and only by users with priveledge to read the file |
| Minimized Redundancy | None. No effort at all |
| Data Security | Your operating system worries about this. Not this module |
| Easiness in Data Management | An easy to get started system |
| Data Structuring | None. You worry about that. |
| Querying Language | Two methods! Thats all you get. |

## Authors

- Github: [Elias Amha](https://www.github.com/0xecho)
- LinkedIn: [Elias Amha](https://www.linkedin.com/in/elijahma)


## Contributing

Contributions are always welcome!



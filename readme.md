# Nepali Calendar Date Converter

This repository hosts pre-converted dates from AD to BS (Bikram Sambat) for the period from April 14, 1943, to April 14, 2043.

## Usage

You can access the pre-converted BS date for any AD date within the specified range directly via a raw URL. For example:

```
https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToBS/1943-04-14
```

Simply replace `1943-04-14` in the URL with the desired AD date to get the corresponding BS date.

### Example

To get the BS date for April 14, 1943, you can use:

```
https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToBS/1943-04-14
```

### Accessing the BS Date Using `curl` or `fetch`

You can use `curl` or `fetch` in your scripts to access the BS date:

**Using `curl`**

```sh
curl https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToBS/1943-04-14
```

**Using `fetch` in JavaScript**

```javascript
fetch('https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToBS/1943-04-14')
    .then(response => response.text())
    .then(data => console.log(data));
```

## Main Generator Logic

The `generate.py` file is included to maintain the main generator logic. While anyone can fork the repository and regenerate the files, it is generally unnecessary for dates till 2043 AD (2099 BS).

## Project Structure

- `generate.py`: Script to generate the folder structure and files with BS dates.
- `requirements.txt`: Python dependencies for the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

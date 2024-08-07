# Nepali Calendar Github

This repository hosts pre-converted dates between the AD (Gregorian) and BS (Bikram Sambat) calendars for the period from April 14, 1943, to April 14, 2043.

## Endpoints

### GET BS

You can access the pre-converted BS date for any AD date within the specified range directly via a raw URL. For example:

```
https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToBS/1943-04-14
```

Simply replace `1943-04-14` in the URL with the desired AD date to get the corresponding BS date.

#### Example

To get the BS date for April 14, 1943, you can use:

```
https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToBS/1943-04-14
```

### GET AD

Similarly, you can access the pre-converted AD date for any BS date within the specified range directly via a raw URL. For example:

```
https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToAD/2000-01-01
```

Simply replace `2000-01-01` in the URL with the desired BS date to get the corresponding AD date.

#### Example

To get the AD date for Baishakh 1, 2000, you can use:

```
https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToAD/2000-01-01
```

### Accessing the Dates Using `curl` or `fetch`

You can use `curl` or `fetch` in your scripts to access the dates:

#### Using `curl`

**Convert to BS**

```sh
curl https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToBS/1943-04-14
```

**Convert to AD**

```sh
curl https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToAD/2000-01-01
```

#### Using `fetch` in JavaScript

**Convert to BS**

```javascript
fetch('https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToBS/1943-04-14')
    .then(response => response.text())
    .then(data => console.log(data));
```

**Convert to AD**

```javascript
fetch('https://raw.githubusercontent.com/AnmupOnline/nepalicalendar/main/convertToAD/2000-01-01')
    .then(response => response.text())
    .then(data => console.log(data));
```

## Main Generator Logic

The `generate.py` file is included to maintain the main generator logic. While anyone can fork the repository and regenerate the files, it is generally unnecessary for dates till 2043 AD (2099 BS).

## Project Structure

- `generate.py`: Script to generate the folder structure and files with BS and AD dates.
- `requirements.txt`: Python dependencies for the project.
- `convertToBS`: Folder contains all the ad to bs conversions.
- `convertToAD`: Folder contains all the bs to ad conversions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

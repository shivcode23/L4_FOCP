import sys
import argparse
from tabulate import tabulate

def display_race_results(fileName, driverFileName):
    try:
        # Read driver details from the specified file or default to 'f1_drivers.txt'
        with open(driverFileName, "r") as driverFile:
            driver_data = {line.split(",")[1]: line.strip().split(",")[2:] for line in driverFile}

    except FileNotFoundError:
        print(f"\nError: The driver details file '{driverFileName}' was not found.")
        print("Please make sure the file exists and the file name is correct.\n")
        return
    except Exception as e:
        print(f"\nAn unexpected error occurred while reading the driver details file '{driverFileName}'.")
        print("Please check the file and try again.\n")
        return

    try:
        with open(fileName, "r") as lapTimeFile:
            raceName = lapTimeFile.readline().strip()
            print(f"Race Name : {raceName}")

            riderIdAndLap = [line.strip() for line in lapTimeFile][1:]
            riderIdInLap = tuple(set([value[:3] for value in riderIdAndLap]))

            result = [[float(value[3:]) for value in riderIdAndLap if prefix in value] for prefix in riderIdInLap]
            riderAndTheirLapTime = {key: value for key, value in zip(riderIdInLap, result)}

            raceInfo = []
            totalLapTime = 0
            for keys, values in riderAndTheirLapTime.items():
                fastest_lap = min(values)
                avg_lap = sum(values) / len(values)
                raceInfo.append((keys, fastest_lap, avg_lap))
                totalLapTime += sum(values)

            # Beautify output using tabulate
            headers = ["Driver Code", "Driver Name", "Car Model", "Fastest Lap Time", "Average Lap Time"]
            table = [
                (keys, driver_data[keys][0], driver_data[keys][1], f"{fastest_lap:.3f}", f"{avg_lap:.3f}")
                for keys, fastest_lap, avg_lap in raceInfo
            ]

            # Print formatted header
            print("\n" + "="*50)
            print(" FASTEST TIME FOR EACH DRIVER ".center(50, "="))
            print("="*50 + "\n")

            print(tabulate(table, headers=headers, tablefmt="grid"))

            avg_lap_time = totalLapTime / len(riderIdAndLap)
            print(f"\nAverage Lap Time for Entire Race: {avg_lap_time:.3f}\n")

            listing = [tupleValue for tupleValue in raceInfo]
            listing_sorted = sorted(listing, key=lambda x: x[1])
            
            # Printing sorted listing with details
            print("Sorted listing of drivers based on fastest lap times:")
            sorted_headers = ["Driver Code", "Driver Name", "Car Model", "Fastest Lap Time"]
            sorted_table = [
                (keys, driver_data[keys][0], driver_data[keys][1], f"{fastest_lap:.3f}")
                for keys, fastest_lap, avg_lap in listing_sorted
            ]
            print(tabulate(sorted_table, headers=sorted_headers, tablefmt="grid"))

            lowestLap = min([lap[1] for lap in listing])
            winnerDriverId = [tupleValue[0] for tupleValue in raceInfo if tupleValue[1] == lowestLap][0]

            print(f"The Winner of This Race is {winnerDriverId}")
            winner_details = {
                "Jersey No.": [k for k, v in driver_data.items() if v[0] == driver_data[winnerDriverId][0]][0],
                "Driver Code": winnerDriverId,
                "Winner Name": driver_data[winnerDriverId][0],
                "Winner Car Model": driver_data[winnerDriverId][1]
            }
            print("\nDetails:")
            print(tabulate(winner_details.items(), tablefmt="grid"))

    except FileNotFoundError:
        print(f"\nError: The race details file '{fileName}' was not found.")
        print("Please make sure the file exists and the file name is correct.\n")
    except Exception as e:
        print(f"\nAn unexpected error occurred while reading the race details file '{fileName}'.")
        print("Please check the file and try again.\n")

def main():
    parser = argparse.ArgumentParser(description="Process F1 race results and display detailed information.")
    parser.add_argument('-r', '--racedetails', help="The file containing race lap times.")
    parser.add_argument('-d', '--driverdetails', default='f1_drivers.txt', help="The file containing driver details (default: f1_drivers.txt).")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

    # Print help if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    try:
        # Manually parse key=value arguments
        race_file = None
        driver_file = 'f1_drivers.txt'
        for arg in sys.argv[1:]:
            if arg.startswith("racedetails="):
                race_file = arg.split("=")[1]
            elif arg.startswith("driverdetails="):
                driver_file = arg.split("=")[1]

        # Parse standard argparse arguments
        args = parser.parse_args()

        # Override with values from argparse if provided
        if args.racedetails:
            race_file = args.racedetails
        if args.driverdetails:
            driver_file = args.driverdetails

        if race_file:
            display_race_results(race_file, driver_file)
        else:
            print("\nError: Race details file must be provided.")
            parser.print_help()
    except argparse.ArgumentError as e:
        print("\nError: Missing or incorrect arguments.\n")
        parser.print_help()

if __name__ == "__main__":
    main()
import fastf1

def main():
    session = fastf1.get_session(2024, "Monaco", "R")

    print("Loading session data...")
    session.load(laps = True, telemetry = False, weather = False)

    print("Session loaded!")

    laps = session.laps

    # pick one driver
    verstappen = laps.pick_drivers("VER")
    verstappen["LapTimeSeconds"] = verstappen["LapTime"].dt.total_seconds()

    leclerc = laps.pick_drivers("LEC")
    leclerc["LapTimeSeconds"] = leclerc["LapTime"].dt.total_seconds()


    print("VER\n", verstappen[["LapNumber", "LapTime"]])
    # laps.groupby()

    print("LEC\n", leclerc[["LapNumber", "LapTime"]])

    print("\nVerstappen Fastest Lap:")
    print(verstappen["LapTimeSeconds"].min(), " seconds")

    print("\nLeclerc Fastest Lap:")
    print(leclerc["LapTimeSeconds"].min(), " seconds")


    print("\nVerstappen Average Lap:")
    print(verstappen["LapTimeSeconds"].mean(), " seconds")

    print("\nLeclerc Average Lap:")
    print(leclerc["LapTimeSeconds"].mean(), " seconds")


    print("\nVerstappen Slowest Lap:")
    print(verstappen["LapTimeSeconds"].max(), "seconds")

    print("\nLeclerc Slowest Lap:")
    print(leclerc["LapTimeSeconds"].max(), " seconds")

if __name__ == "__main__":
    main()
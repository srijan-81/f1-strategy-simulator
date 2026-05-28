import fastf1

def main():
    session = fastf1.get_session(2024, "Monaco", "R")
    session.load

    print("Loading session data...")
    session.load(laps = True, telemetry = False, weather = False)

    print("Session loaded!")

    laps = session.laps
    print(laps.head())

if __name__ == "__main__":
    main()
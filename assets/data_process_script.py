from base.base import AcquireDataJob


def main():
    df = AcquireDataJob("data").load_raw_data()
    print(f"#### Below are some top records ####")
    print(df.head())


if __name__ == '__main__':
    main()

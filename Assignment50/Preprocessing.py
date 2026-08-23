from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def PreprocessData(df):

    print("\n----- Data Preprocessing -----")

    print("\nMissing Values:")
    print(df.isnull().sum())

    if df.isnull().sum().sum() > 0:
        print("\nNull values found. Removing rows...")
        df.dropna(inplace=True)
    else:
        print("\nNo null values found.")
    
    X = df.drop("target", axis=1)
    Y = df["target"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.20,random_state=42)

    print("\nTraining Data Shape:", X_train.shape)
    print("Testing Data Shape:", X_test.shape)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, Y_train, Y_test
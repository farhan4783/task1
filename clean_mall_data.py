import pandas as pd # type: ignore


df = pd.read_csv('Mall_Customers.csv')


print("Initial Data Overview:")
print(df.info())
print(df.head())

# 2. Handle missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


df.dropna(inplace=True)

df.drop_duplicates(inplace=True)


df['Gender'] = df['Gender'].str.strip().str.capitalize()




df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

# 7. Fix data types
df['age'] = df['age'].astype(int)


print("\nCleaned Data Overview:")
print(df.info())
print(df.head())

# 9. Save cleaned data
df.to_csv('Cleaned_Mall_Customers.csv', index=False)
print("\n✅ Cleaned dataset saved as 'Cleaned_Mall_Customers.csv'")

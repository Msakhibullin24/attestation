# Анализ категориальных переменных
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
print(df[categorical_cols].describe().T)  # Показывает count, unique, top, freq для каждой категориальной переменной

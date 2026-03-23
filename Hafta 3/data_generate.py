import pandas as pd
import numpy as np

def generate_health_data(num_samples=500, random_seed=42):
    """
    Generates a synthetic healthcare dataset with KanSekeri and Tansiyon columns.
    
    Args:
        num_samples (int): The number of rows to generate.
        random_seed (int): Seed for reproducibility.
        
    Returns:
        pd.DataFrame: The generated synthetic dataset.
    """
    np.random.seed(random_seed)
    
    # KanSekeri: Normal distribution with mean=100, std=15
    kan_sekeri = np.random.normal(loc=100, scale=15, size=num_samples)
    
    # Tansiyon: Normal distribution with mean=120, std=10
    tansiyon = np.random.normal(loc=120, scale=10, size=num_samples)
    
    # Create the DataFrame
    df = pd.DataFrame({
        'KanSekeri': kan_sekeri,
        'Tansiyon': tansiyon
    })
    
    # Ensure values are rounded to 1 decimal place for realism
    df['KanSekeri'] = df['KanSekeri'].round(1)
    df['Tansiyon'] = df['Tansiyon'].round(1)
    
    return df

if __name__ == "__main__":
    # Generate the dataset
    print("Veri seti oluşturuluyor...")
    df_health = generate_health_data(num_samples=500)
    
    # Save to CSV
    output_filename = "veri.csv"
    df_health.to_csv(output_filename, index=False)
    
    print(f"Veri seti başarıyla oluşturuldu ve '{output_filename}' dosyasına kaydedildi.")
    print(f"Satır sayısı: {len(df_health)}")
    print("\nİlk 5 satır:")
    print(df_health.head())

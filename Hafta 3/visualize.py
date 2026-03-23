import pandas as pd
import matplotlib.pyplot as plt

def visualize_health_data(csv_filename="veri.csv"):
    """
    Reads the health dataset from a CSV file and plots histograms 
    for KanSekeri and Tansiyon.
    
    Args:
        csv_filename (str): The path to the CSV file.
    """
    try:
        # Load the dataset
        df = pd.read_csv(csv_filename)
        
        # Check if the required columns exist
        if not {'KanSekeri', 'Tansiyon'}.issubset(df.columns):
            print("Hata: CSV dosyasında 'KanSekeri' ve 'Tansiyon' sütunları bulunamadı.")
            return

        print(f"'{csv_filename}' başarıyla yüklendi. Grafikler çiziliyor...")

        # Plotting
        plt.figure(figsize=(12, 5))

        # Histogram for KanSekeri
        plt.subplot(1, 2, 1) # 1 row, 2 columns, 1st subplot
        plt.hist(df['KanSekeri'], bins=30, color='skyblue', edgecolor='black', alpha=0.7)
        plt.title('Kan Şekeri Dağılımı (µ=100, σ=15)', fontsize=14)
        plt.xlabel('Kan Şekeri Değeri', fontsize=12)
        plt.ylabel('Frekans', fontsize=12)
        plt.grid(axis='y', alpha=0.5)

        # Histogram for Tansiyon
        plt.subplot(1, 2, 2) # 1 row, 2 columns, 2nd subplot
        plt.hist(df['Tansiyon'], bins=30, color='lightcoral', edgecolor='black', alpha=0.7)
        plt.title('Tansiyon Dağılımı (µ=120, σ=10)', fontsize=14)
        plt.xlabel('Tansiyon Değeri', fontsize=12)
        plt.ylabel('Frekans', fontsize=12)
        plt.grid(axis='y', alpha=0.5)

        # Adjust layout and show
        plt.tight_layout()
        plt.show()
        
    except FileNotFoundError:
        print(f"Hata: '{csv_filename}' dosyası bulunamadı. Lütfen önce veri üretme scriptini çalıştırın.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    visualize_health_data()

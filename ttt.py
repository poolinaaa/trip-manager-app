from datetime import datetime, timedelta
data = {
  "base": "EUR",
  "end_date": "2012-05-03",
  "rates": {
    "2012-05-01": {
      "AUD": 1.278047,
      "CAD": 1.302303,
      "USD": 1.322891
    },
    "2012-05-02": {
      "AUD": 1.274202,
      "CAD": 1.299083,
      "USD": 1.315066
    },
    "2012-05-03": {
      "AUD": 1.280135,
      "CAD": 1.296868,
      "USD": 1.314491
    }
  },
  "start_date": "2012-05-01",
  "success": True,
  "timeseries": True
}

# Tworzenie osobnych list dla każdej waluty
aud_rates = []
cad_rates = []
usd_rates = []

# Pobieranie dat początkowej i końcowej
start_date = data["start_date"]
end_date = data["end_date"]

# Przechodzenie przez daty i dodawanie wartości do odpowiednich list
current_date = start_date
while current_date <= end_date:
    rates_for_date = data["rates"][current_date]
    aud_rates.append(rates_for_date["AUD"])
    cad_rates.append(rates_for_date["CAD"])
    usd_rates.append(rates_for_date["USD"])
    current_date = (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")

# Wyświetlanie wyników
print("AUD rates:", aud_rates)
print("CAD rates:", cad_rates)
print("USD rates:", usd_rates)
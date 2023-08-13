from geopy.geocoders import Nominatim
def main():
  locator = Nominatim(user_agent = "myapp")
  def Coordinates(address):
      location = locator.geocode(f"{address}")
      print(location.latitude, location.longitude)
      print(location.point)
  Destination = input("Enter the location you want to go ")
  Start =  input("Enter the location you are at ")
  print("Coordinates of Start: ")
  Coordinates(Start)
  print("Coordinates of Destination: ")
  Coordinates(Destination)
if __name__ =='__main__':
  main()


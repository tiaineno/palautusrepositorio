from luo_peli import luo_peli

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        peli = luo_peli(vastaus)

        if not peli:
            break
        
        peli.pelaa()

if __name__ == "__main__":
    main()

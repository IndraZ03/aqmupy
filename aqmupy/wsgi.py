from flask import Flask, jsonify,request,make_response
app = Flask(__name__)
import json
from whatsapp_api_client_python import API

@app.route('/')
@app.route('/api/', methods= ['POST', 'GET'])

def api():

    if request.method == "POST":

        

        greenAPI = API.GreenApi(
    "1101806751", "63015a43115a4ed58f340756ac948c105b2a4cf63f664db123"
        )
        data = request.get_json()
        alert = data.get("alert")
        tanggal = data.get("tanggal")
        jam = data.get("jam")
        lokasi = data.get("lokasi")
        penerima = data.get('penerima')
        hp = str(data.get('hpPenerima'))
        lat = data.get("lat")
        lon = data.get("lon")
        temp = data.get("suhu")
        hum = data.get('hum')
        kCO = data.get("kCO")
        ISPU = data.get("ISPU")
        kategori = data.get("kategori")
        PM25 = data.get('pm25')
        PM10 = data.get('pm10')
        cemar = data.get('cemar')
        
        try:
            with open('data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
                
            
        except Exception as e:
            return jsonify({"error": str(e)})

        if alert == "pku":
            pesan = f'''
            
*PERINGATAN POLUSI UDARA*

Kepada yang terhormat {penerima},

Tanggal : {tanggal}
Waktu : {jam}
Lokasi : {lokasi}

Berdasarkan data kualitas udara yang kami kumpulkan melalui wahana tanpa awak, kami mengidentifikasi bahwa terjadi polusi udara pada kawasan {lokasi} memiliki skala ISPU dengan kategori {kategori} Berikut detail data lebih lanjut :


*Data Kualitas Udara*
nilai ISPU : {ISPU}
kategori : {kategori}
kadar : {kCO} ppm
PM2.5 : {PM25} (µg/m3)
PM10 : {PM10} (µg/m3)
Responsible pollution : {cemar}
suhu udara : {temp}
kelembapan : {hum}

Kami akan terus memantau situasi ini dan akan memberikan pembaruan secara berkala. Semoga informasi ini dapat ditindaklanjuti dan menjadi referensi untuk mengambil kebijakan dalam mengurangi polusi karbonmonoksida.
Terima kasih.

Hormat kami,

*AURORA STMKG*
Kontak darurat : 089666444301(indra)

            '''
            if kategori == "Tidak Sehat":
                tindakan = """
1.Hindari aktivitas fisik yang berat di luar ruangan.
2.Gunakan masker pelindung jika Anda harus keluar.
3.Tetap di dalam ruangan yang tertutup dan ber-AC jika memungkinkan."""
            elif kategori == "Sangat Tidak Sehat":
                tindakan = '''
1. Batasi aktivitas di luar ruangan.
2. Gunakan masker pelindung saat berada di luar.
3.Pertimbangkan untuk tetap di dalam ruangan yang memiliki sirkulasi udara yang baik.'''
            elif kategori == "Berbahaya":
                tindakan = '''
1. Jangan keluar rumah kecuali dalam situasi darurat.
2. Tetap di dalam ruangan yang tertutup dan beralih ke sumber udara dalam ruangan yang bersih.
3. Gunakan peralatan penjernih udara dalam ruangan jika tersedia.
                        '''
        
       
            pesan1 = f'''
*Tindakan yang dianjurkan ketika polusi udara pada kategori {kategori}*:
            {tindakan}
            '''

            if cemar == "CO":
    
                pesan2 = f'''
*Tindakan yang dapat mengurangi emisi karbonmonoksida* :
1. Perketat pengawasan terhadap industri yang berpotensi menghasilkan emisi CO berlebih.
2. Perketat pengawasan terhadap aktivitas ilegal yang berpotensi menyebabkan kebakaran hutan.
3. Mendorong penggunaan energi alternatif yang ramah lingkungan.
4. Meningkatkan daya tarik penggunaan transportasi umum.
5. Menetapkan standar emisi yang ketat dan melakukan inspeksi secara rutin.
            '''
            elif cemar == "PM10" or "PM2.5":
                pesan2 =f'''
*Tindakan yang dapat mengurangi emisi PM* :
1. Perketat pengawasan terhadap industri yang berpotensi menghasilkan emisi partikulat halus.
2. Perketat pengawasan terhadap aktivitas ilegal yang berpotensi menyebabkan kebakaran hutan.
3. Mendorong penggunaan energi alternatif yang ramah lingkungan.
4. Meningkatkan daya tarik penggunaan transportasi umum.
5. Menetapkan standar emisi yang ketat dan melakukan inspeksi secara rutin. '''
                
            response = greenAPI.sending.sendMessage(f"{hp}@c.us", pesan)
            response = greenAPI.sending.sendMessage(f"{hp}@c.us", pesan1)
            response = greenAPI.sending.sendMessage(f"{hp}@c.us", pesan2)
                        

        elif alert == "pkh":
            pesan = f'''

*PERINGATAN KEBAKARAN HUTAN*
Kepada yang terhormat {penerima},

Tanggal : {tanggal}
Waktu : {jam}
Lokasi : {lokasi}

Berdasarkan data kualitas udara dan meteorologi yang kami kumpulkan melalui wahana tanpa awak, kami mengidentifikasi adanya indikasi kebakaran hutan pada kawasan {lokasi} dengan detail berikut :


*Data Meteorologi*
suhu udara : {temp}
kelembapan : {hum}

*Data Kualitas Udara*
nilai ISPU : {ISPU}
kategori : {kategori}
kadar CO : {kCO} ppm
PM2.5 : {PM25} (µg/m3)
PM10 : {PM10} (µg/m3)

Kami akan terus memantau situasi ini dan akan memberikan pembaruan secara berkala. Semoga informasi ini dapat ditindaklanjuti dan menjadi referensi untuk mengambil kebijakan untuk memitigasi kebakaran hutan.
Terima kasih.

Hormat kami,

*AURORA STMKG*
Kontak darurat : 089666444301(indra)
        '''
            response = greenAPI.sending.sendMessage(f"{hp}@c.us", pesan)

        elif alert == "ppkh":
            pesan = f'''
*PERINGATAN KAWASAN BERPOTENSI KEBAKARAN HUTAN*

Kepada yang terhormat {penerima},

Tanggal : {tanggal}
Waktu : {jam}
Lokasi : {lokasi}

Berdasarkan data kualitas udara dan meteorologi yang kami kumpulkan melalui wahana tanpa awak, kami mengidentifikasi adanya indikasi kebakaran hutan pada kawasan {lokasi} dengan detail berikut :
            
*Data Meteorologi*
suhu udara : {temp}
kelembapan : {hum}

*Data Kualitas Udara*
nilai ISPU : {ISPU}
kategori : {kategori}
kadar : {kCO} ppm
PM2.5 : {PM25} (µg/m3)
PM10 : {PM10} (µg/m3)

Tindakan yang dianjurkan :
Mohon agar warga sekitar diberikan himbauan untuk tetap waspada terhadap risiko kebakaran hutan. Jika ada tanda-tanda asap atau api, segera kirim petugas pemadam kebakaran.
Kami akan terus memantau situasi ini dan akan memberikan pembaruan secara berkala. Semoga informasi ini dapat ditindaklanjuti dan menjadi referensi untuk mengambil kebijakan untuk mengantisipasi kebakaran hutan.

Terima kasih.

Hormat kami,

*AURORA STMKG*
Kontak darurat : 089666444301(indra)'''
            

            response = greenAPI.sending.sendMessage(f"{hp}@c.us", pesan)

        print(response.data)

        return info()

    

        
    elif request.method == "GET":
        info()



def info():      
        try:
         with open('data.json', 'r') as json_file:
            saved_data = json.load(json_file)
                
            return jsonify(saved_data)
        except Exception as e:
            return jsonify({"error": str(e)})
   


if __name__ == '__main__':
    app.run(debug=True)

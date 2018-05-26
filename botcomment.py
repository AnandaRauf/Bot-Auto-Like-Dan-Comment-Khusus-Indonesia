print (' ////****** 26 Mei 2018 PT.MrvDevelopment™ ********\\\ ')
print (' Program Bot Like dan Comment ')
print (' Chief Executive Officer Ananda Rauf Maududi ')
import random

butuhautolike=["Butuh auto like?<name>?","hubungi saya!!! <name> ^^","follow Instagram: @anandarauf02","Linkenidn: Ananda Rauf Maududi <name>","IT Senior","Consultant? <name> inbox saya, terima kasih ^^"]

butuhprogram=["Butuh jasa pembuatan program dan aplikasi android? <name> :)","hubungi saya saja <name>?","100% Terpercaya\n<name> dijamin memuaskan!","<name> terima kasih","selamat beraktivias kembali, dan salam satu jiwa IT  :)","Kabupaten Bogor <name> Bojong Kulur"]

ngambek=("<name> knapa?","jangan ngambek dong <name> :v","waduh <name> ngambek nih..","hhhh knapa <name>?","ada apa <name>?",)

lapor=("siap..\nLaporan diterima","laporan diterima","ya.. laporan diterima","ya.. terimakasih atas laporannya","ok prajurit laporan diterima","siap pak\nlaporan diterima","ok laporan yang bagus","disini jg mau melapor...\nehh tadi mau nulis apa yah? :v","siap","laporan <name> (y)",)

sakit=["sakit knapa <name>?","<name> sakit yh?",":(","wah <name> sakit knapa?\ncepat sembuh yh <name>","bawa ke rumah sakit kalo lagi sakit tu <name>","sakitnya tuh disini :v","waduuhh <name> lagi sakit nih kawan-kawan :v","dua tiga perahu rakit.. ternyata <name> lagi sakit :v","wah yg sabar yah <name>","sakit minum obat dong :v","wiu wiu wiu.. ambulan datang :v",]

dadar=("minta dadarnya dong <name> :v","wah enak tuh kayaknya..","dadar itu bukannya yg dibadan yh? #herp","dadar gulung bukan yah?","dadar telor kah? :v","dadar di goreng dadakan #sound_SFX_tahubulat","mantap","dadarnya enak","waw","wihh dadar nih :D","wew","he","hihihi","nyoba dikit boleh dong dadarnya <name> :v","waw aku mau...","mau banget","ehh ada dadar nih..",)

beb=("bebeb aku tuh <name> :v","wah itu kan bebebku :v","HL, ADBBQ GK DST #axis_warbyazah :v","beb ku diambil sama <name> nih :v","bebeb ku itu oi :v","ciee bebeb orang itu cuy :v")

disita=(
"wahh disita knapa <name>? :v","makanya bayar pajak kalo gak mau disita :v\nwkwkwk","ciee disita :v","hhhh","disita ?\nwaw aku terkejut :v","cie kena sita yah <name> ? :v","rasain :v\nwkwkwkwk","aduh kena sita.. kasian :v","bhahaha disita :v #ntapz","wekwekwek kena sita :v","wkwkwk disita",
)
diadd=("boleh lah","gak mau :v","add aja sendiri :v","ngeadd?\nwaw aku tercengang :v","add sendiri kan bisa :3","cie adm ya? :v","BL kk 500 orang, diadd dong..blablabla... adm oh adm","wek gak mau :v","bayar dlu 50rb :v","hhhh ngeadd ?","duhh minta di add..\nadd aja sendiri :v")
cari=("lagi nyari apa nih <name>?","coba cari di bukalapak dot com :v","moga sukses nyarinya <name> :)","<name> lagi nyari apa?","<name> nyari sesuatu?","<name> cari apa?","coba cari di tokopedia dot com :v",)
ntaps=("ntaps sekali kk :v","wah ntaps bos <name>","ntaps cuy :v","ntaps :v","waw ntaps sekali kk :v")
sepi=("sekarang ada aku nih <name> jadi gak sepi lagi...","pada kmana ya <name>?","sepi ya?","ku koment distatus <name> biar gak sepi lg :v","hadir distatus <name> untuk meramaikan","tenang <name>\nwalapun sepi aku tetap komen untuk meramaikan :v","kalo mau rame di pasar sana :v","wah sepi nih..","sepi juga yah","sepi... 0,0","hha sepi nih distatus <name>","pokoknya aku ramaikan walapun sepi..","sepi","yes akhirnya sepi jg :v")
nyimpen=("nyimpen apa kk?","asal jgn nyimpen selingkuhan aja :v","nyimpen apa nih <name>?","wah <name> bikin penasaran aja pake disimpen2 segala :v","nyimpen apa <name>?","disimpen dimana <name>?",) 
rindu=("ciee lagi rindu yah <name>? :v","wah :O","rindu sama aku kah? :v","ciee aku juga rindu sama <name> :v",
)
bahagia=("ciee lagi bahagia nih <name> :v","ciee yg lg bahagia :v",":v","hhhh","hehe",)

mana=("mana apanya <name>??","mungkin itu","yg itu kali <name>","mana yah...","bingung yg mana..","hehe itu aja")



#jika ada teman yang pake kata" ini
com_match={
"butuhautolike":"%s"%butuhautolike[random.randrange(0,len(butuhautolike))],"butuh program":'%s'%butuhprogram[random.randrange(0,len(butuhprogram))],
"-_-":"%s"%ngambek[random.randrange(0,len(ngambek))],"lapor":"%s"%lapor[random.randrange(0,len(lapor))],"dadar":"%s"%dadar[random.randrange(0,len(dadar))]," beb":beb[random.randrange(0,len(beb))],"disita":"%s"%disita[random.randrange(0,len(disita))],"diadd":"%s"%diadd[random.randrange(0,len(diadd))],"cari":"%s"%cari[random.randrange(0,len(cari))],
"ntaps":"%s"%ntaps[random.randrange(0,len(ntaps))]
,"sepi":"%s"%sepi[random.randrange(0,len(sepi))],
"nyimpen":"%s"%nyimpen[random.randrange(0,len(nyimpen))],"rindu":"%s"%rindu[random.randrange(0,len(rindu))],
"bahagia":"%s"%bahagia[random.randrange(0,len(bahagia))],"mana":"%s"%mana[random.randrange(0,len(mana))],
}

# comment biasa
com=["gubrak!\nSaya terkejut melihat status ini :v",
"status <name> #warbyazah","paling suka nongkrong di status <name>","walaupun sinyal suka ngilang.. aku tetap komen distatus <name> :v",
"Hai <name>? :D","tadi kan aku liat branda.. ehh ada status <name>\nyaudah aku koment aja :v","wah status <name> luarbiasa (y)","akhirnya <name> update status juga :v","waw aku tercengang :v","hehe numpang lewat <name>","nitip sendal","brum brum... misi mobil orang kaya lewat 8|\nwkwkwk","ehh kebetulan <name> bikin status nih..\naku koment ya <name> :)","dari <name> jones sampai sekarang..\nstatus <name> selalu mantap :v",
"dari tahun ke tahun status <name> selalu enak dibaca (y)","<name> status kamu bagus banget (y)","oh ya.. mampir dlu ahh di statusnya <name>","status anda #warbyazah","waw status yang sangat #warbyazah","status <name> paling aku suka (y)","status <name> selalu ada di branda ku :v","ngeng ngeng..  misi mau ngebut dlu...\nwkwkwk","wiu wiu wiu... minggir mobil polisi lewat :D","#warbyazah","ciee update status nih yah :v","hai <name>","status <name> adalah tempat nongkrong ku yg paling mantap","hehe","hihi","haaa... <name> update status nih... :v","lagi apa <name>?","waduh <name> udah update status aja nih :v"]

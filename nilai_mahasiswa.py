class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nim: str, nama: str, nilai_tugas: float, nilai_uts: float):
        self.nim = nim
        self.nama = nama

        self.__nilai_tugas = 0.0
        self.__nilai_uts = 0.0

        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts

        Mahasiswa.jumlah_mahasiswa += 1

    @property
    def nilai_tugas(self) -> float:
        return self.__nilai_tugas

    @nilai_tugas.setter
    def nilai_tugas(self, nilai: float):
        if not (0 <= nilai <= 100):
            raise ValueError("Nilai tugas harus berada di rentang 0 - 100.")
        self.__nilai_tugas = float(nilai)

    @property
    def nilai_uts(self) -> float:
        return self.__nilai_uts

    @nilai_uts.setter
    def nilai_uts(self, nilai: float):
        if not (0 <= nilai <= 100):
            raise ValueError("Nilai UTS harus berada di rentang 0 - 100.")
        self.__nilai_uts = float(nilai)

    def rata_rata_sementara(self) -> float:
        return (self.__nilai_tugas + self.__nilai_uts) / 2

    def predikat(self) -> str:
        rata = self.rata_rata_sementara()
        if rata >= 85:
            return "A"
        elif rata >= 75:
            return "B"
        elif rata >= 60:
            return "C"
        elif rata >= 50:
            return "D"
        else:
            return "E"

    @classmethod
    def info_jumlah_mahasiswa(cls) -> str:
        return f"Total mahasiswa terdaftar: {cls.jumlah_mahasiswa}"

    @staticmethod
    def validasi_nim(nim: str) -> bool:
        return nim.isdigit() and len(nim) >= 6


class RekapNilaiKelas:
    def __init__(self, nama_kelas: str, mata_kuliah: str):
        self.nama_kelas = nama_kelas
        self.mata_kuliah = mata_kuliah
        self.daftar_mahasiswa = []

    def tambah_mahasiswa(self, mhs: Mahasiswa):
        if not Mahasiswa.validasi_nim(mhs.nim):
            print(f"[GAGAL] NIM '{mhs.nim}' tidak valid untuk {mhs.nama}.")
            return
        self.daftar_mahasiswa.append(mhs)
        print(f"[OK] {mhs.nama} ({mhs.nim}) masuk ke rekap {self.nama_kelas}.")

    def cetak_rekap(self):
        print(f"\n=== REKAP NILAI {self.nama_kelas} - {self.mata_kuliah} ===")
        if not self.daftar_mahasiswa:
            print("Belum ada data mahasiswa.")
            return

        for mhs in self.daftar_mahasiswa:
            print(
                f"NIM: {mhs.nim} | Nama: {mhs.nama} | "
                f"Tugas: {mhs.nilai_tugas:.1f} | UTS: {mhs.nilai_uts:.1f} | "
                f"Rata-rata: {mhs.rata_rata_sementara():.2f} | Predikat: {mhs.predikat()}"
            )
        print()


if __name__ == "__main__":

    mhs_1 = Mahasiswa("2501001", "Dina", 88, 84)
    mhs_2 = Mahasiswa("2501002", "Raka", 76, 80)
    mhs_3 = Mahasiswa("123", "Budi", 70, 72)  # Contoh NIM tidak valid

    mhs_2.nilai_uts = 86
    print(f"Nilai UTS baru {mhs_2.nama}: {mhs_2.nilai_uts}")

    rekap = RekapNilaiKelas("3B KOM", "Pemrograman Berorientasi Objek")
    rekap.tambah_mahasiswa(mhs_1)
    rekap.tambah_mahasiswa(mhs_2)
    rekap.tambah_mahasiswa(mhs_3)

    rekap.cetak_rekap()

    print(Mahasiswa.info_jumlah_mahasiswa())
import time
import dxchange
from ganrec.utils import nor_phase
from ganrec.ganrec2 import GANphase

def main():
    energy = 10
    z = 0.5
    pv = 5e-7
    iter_num = 1000
    fname_data = '/data/gan_phase/ifp_shepp.tiff'
    data = dxchange.read_tiff(fname_data)
    px, _ = data.shape
    data = nor_phase(data)
    gan_phase_object = GANphase(data, energy, z, pv,  iter_num)
    start = time.time()
    rec = gan_phase_object.recon
    end = time.time()
    print('Running time is {}'.format(end - start))
    dxchange.write_tiff(rec.reshape((px, px)), '/data/gan_phase/test', overwrite=True)


if __name__ == "__main__":
    main()
import os, qrcode

def generate(msg, filename=None, save=False):
    '''
    Generate and return QR code encoding msg
    Export it to `qrcodes` directory by setting `save` flag
    '''

    img = qrcode.make(msg)
    
    if save:
        if not filename:
            filename = '_'.join(filename.lower().spit())
            filename = f'{filename}.png'

        save_path = f'qrcodes/{filename}'
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        img.save(save_path)
    
    return img


if __name__ == '__main__':
    vaccines = ['tetanus', 'penicillin']
    clinics = [i + 1 for i in range(3)]

    for vaccine in vaccines:
        for clinic in clinics:
            msg = f'{vaccine} vaccine, deliver to clinic {clinic}'.capitalize()
            filename = f'{vaccine}_clinic_{clinic}.png'

            generate(msg, filename, save=True)
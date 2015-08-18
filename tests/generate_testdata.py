# Released under The MIT License (MIT)
# http://opensource.org/licenses/MIT
# Copyright (c) 2013 SCoT Development Team

import numpy as np

global randn_index
global randn


def generate_covsig(covmat, n):
    """generate pseudorandom stochastic signals with covariance matrix covmat"""
    global randn_index
    global randn

    covmat = np.atleast_2d(covmat)
    m = covmat.shape[0]
    l = np.linalg.cholesky(covmat)

    x = []
    while len(x) < n * m:
        to_go = min(randn_index + n * m - len(x), len(randn))
        x.extend(randn[randn_index:to_go])
        randn_index = to_go % len(randn)
    x = np.reshape(x, (m, n))

    # matrix to make cov(x) = I
    d = np.linalg.inv(np.linalg.cholesky(np.atleast_2d(np.cov(x))))

    x = l.dot(d).dot(x)

    return x


# 497 random numbers drawn from the standard normal distribution
#noinspection PyRedeclaration
randn_index = 0
#noinspection PyRedeclaration
randn = [-1.28924940e+00, -5.10070850e-01, 5.68293566e-01,
         -7.61050402e-02, -1.01814943e+00, -7.72800459e-01,
         -1.08905278e+00, 9.58712833e-01, 1.10965728e+00,
         -6.78270453e-01, 3.16533816e-01, -1.27757479e-01,
         -3.62138069e-01, 9.15372186e-01, 5.47984150e-01,
         -1.13324263e-01, -1.34433972e+00, -3.39482406e-01,
         -2.08072033e-01, -8.45049802e-02, 3.55497423e-01,
         -1.34077935e+00, 3.37915043e-01, 7.10498827e-01,
         -6.66169478e-01, 8.45320876e-01, 3.65939944e-01,
         -2.13387617e-01, -4.95729488e-01, -5.59772662e-01,
         -4.74427401e-01, 5.49582620e-01, -6.85502804e-01,
         -3.11679577e-01, 9.21292598e-01, 1.60273660e+00,
         8.50788259e-01, -2.49920711e-02, -8.81468039e-01,
         5.15675436e-01, 2.41348839e-01, 1.11493579e-01,
         -6.62189408e-02, 9.47902721e-01, -1.50506022e+00,
         4.51667808e-01, -3.97496393e-02, -7.81176215e-01,
         1.63202849e-01, 3.71671017e-02, 1.01553423e+00,
         -1.18014928e+00, -8.12127342e-01, -4.62431076e-01,
         -7.51114853e-01, 7.44557410e-01, 1.81455081e+00,
         -3.31350132e-02, 1.10208325e+00, 4.07801581e-01,
         2.45458051e-01, 2.23996795e+00, -9.16067911e-01,
         -4.71496138e-01, 4.90239324e-01, -1.37619382e+00,
         -1.88447998e+00, 4.67428005e-01, -3.90935542e-01,
         -6.36091013e-02, 1.43856374e+00, -1.81477842e+00,
         3.14182181e-03, 1.35273271e-02, -1.79580680e-01,
         3.64600166e-01, 1.11098878e+00, 2.16094975e-01,
         -6.04629176e-01, -1.54129942e+00, 2.05606120e-01,
         7.25569818e-01, 9.90531388e-01, 5.86687178e-01,
         1.14037381e+00, -5.35113838e-01, -8.49546344e-01,
         -8.53812010e-02, -2.65370780e-01, 7.28010794e-01,
         2.57111092e+00, 2.44851628e-01, 3.54347949e-01,
         -3.61868898e-01, -1.55791648e+00, 9.82076514e-01,
         -9.18054545e-01, 1.35889659e+00, -4.47413155e-01,
         -1.10644224e+00, 2.57389695e-01, 7.20545632e-02,
         4.04011692e-01, -4.39789172e-01, 7.23031919e-01,
         8.48632749e-01, -8.62080971e-01, -1.70191854e+00,
         1.55271575e+00, 2.31505047e-01, -2.78973588e-01,
         -2.50991634e-01, 8.54733154e-01, 1.37157436e+00,
         -9.87478318e-01, 4.08798401e-01, 9.06041671e-01,
         -1.53069535e+00, 3.19828762e-01, 9.81580904e-01,
         -2.25585449e+00, 2.81085675e+00, -9.14517500e-02,
         1.01781083e+00, 1.03481778e-01, -1.98671773e-01,
         9.22330630e-01, 1.09209946e-02, -1.82300949e-01,
         -1.45695484e-01, -7.43178649e-01, 3.21031115e-01,
         -1.45624780e+00, 1.21492475e+00, 9.17324378e-01,
         -4.39407575e-01, 7.40533710e-02, 2.10734639e+00,
         1.26665639e+00, 5.59106591e-01, -5.93219926e-01,
         -1.09291823e-01, 8.08168122e-01, 2.88286250e-01,
         -9.03860996e-02, -3.83002554e-01, -1.41805175e+00,
         9.00682607e-01, 1.78803296e-01, -5.50267674e-01,
         1.34184959e+00, -1.72823885e-01, -5.70967035e-02,
         1.10686816e+00, 5.64166132e-02, 1.22963188e-01,
         -6.35587279e-01, 1.02076517e+00, -2.63502839e-01,
         -1.63552493e+00, -2.79223909e-01, 3.27860718e-01,
         1.81003015e-01, 5.63168206e-01, 3.23660950e-01,
         5.56562289e-01, -1.66409653e+00, -8.39465618e-01,
         1.28552893e+00, 4.32557807e-01, 1.12215519e+00,
         -7.42708559e-01, -1.46953958e+00, 1.10411922e+00,
         -2.26442829e+00, 8.65762218e-01, -1.96922599e+00,
         -1.23921543e-01, -1.61339405e+00, -2.48836914e-01,
         1.50612837e-01, 1.11017448e-01, 2.22125957e+00,
         5.90964167e-01, 1.52420729e+00, -3.07737452e-01,
         8.50324924e-01, 4.25688707e-01, 1.55805575e-01,
         1.21427691e-01, 2.19415394e-01, -1.38365556e+00,
         -6.60969015e-01, 1.74100004e+00, 3.37501702e-02,
         1.48877532e+00, 2.04329226e-01, 1.45102754e+00,
         8.95428252e-01, -1.44155973e+00, -1.59526784e+00,
         -1.02551810e-01, -3.35248031e-02, 2.45868038e-01,
         3.00101365e+00, 3.99062307e-01, 1.88931259e+00,
         8.50618487e-01, 2.11490005e+00, -5.71203148e-01,
         -2.73360143e-01, 9.50540031e-01, -6.71667314e-01,
         -3.80147183e-01, 1.82894922e-01, 1.20030787e+00,
         1.54147414e+00, 9.30767127e-02, -1.61388140e-01,
         8.46556546e-01, 8.46822624e-01, 1.79169264e+00,
         -3.94477001e-01, -1.02605659e+00, 6.57472762e-01,
         1.96974043e-01, -8.96923239e-01, 6.08585565e-01,
         -7.66741370e-01, 1.61303993e-01, -4.77239321e-01,
         -7.83064562e-02, -8.02768599e-01, -9.30298564e-01,
         5.11695803e-04, -3.71792254e-01, 1.49259677e+00,
         6.30735175e-01, 1.16876422e-01, 1.23733330e+00,
         6.03886526e-01, 2.30739795e-01, -4.80077551e-01,
         -6.54144362e-01, 3.50541094e-01, -1.04966235e+00,
         -7.67089716e-01, 5.70864007e-01, 3.72064047e-01,
         7.78497116e-01, -1.06429030e+00, 5.95492691e-01,
         1.24678040e+00, 8.86673022e-01, 1.03923951e+00,
         -1.48421542e+00, 3.79737537e-01, -7.43619347e-01,
         -9.65573183e-02, 7.38965002e-01, -7.40115177e-01,
         6.93569925e-01, -5.27267018e-01, -4.12041246e-01,
         -1.57071368e+00, -1.42576383e+00, -9.92510600e-02,
         -1.92046976e+00, 1.79574763e+00, 1.11144197e+00,
         5.05105591e-01, -9.97419026e-01, -1.36617344e-01,
         -7.66826322e-01, 1.18323399e+00, -3.96412410e-01,
         4.31574486e-01, -7.49306564e-01, -5.45035609e-01,
         8.32620445e-01, -1.17796086e+00, 1.63973451e+00,
         7.22324611e-01, -5.11340889e-03, 1.16941706e+00,
         -6.17330915e-01, 8.17834621e-01, 8.07912789e-01,
         -1.09683179e+00, -1.50123848e+00, -4.44879399e-01,
         -3.57987302e-01, -4.25263040e-01, 1.80887485e+00,
         -1.16389545e-01, 7.65489987e-01, -6.92483538e-01,
         -1.36441211e+00, 8.28839577e-01, 8.98499340e-01,
         5.99926211e-01, 8.71733010e-02, 1.57871551e-01,
         8.53661055e-01, 3.23908146e-01, 1.18132955e+00,
         4.57534852e-01, -5.90230038e-01, -7.57532679e-01,
         -1.77502832e+00, -2.96984113e-01, 3.62694458e-01,
         1.82574366e+00, 5.74637359e-01, -2.42540564e+00,
         1.53666915e+00, 1.13279991e+00, -1.47084899e+00,
         7.57416001e-01, -3.71546710e-01, 6.72233787e-01,
         5.26172492e-01, -3.36067121e-01, -1.30489875e-01,
         -2.19963979e+00, 1.42033516e+00, 9.61684293e-01,
         4.31224426e-01, -1.16292188e+00, 8.07461727e-01,
         -2.48138855e-02, -3.04245367e-01, 1.59632176e+00,
         -7.91047448e-01, 2.04868799e-01, 7.21010472e-02,
         1.04699193e+00, -3.35184866e-01, 2.76603517e-01,
         6.57718399e-01, -1.44915141e+00, -4.90758460e-01,
         1.42674760e+00, 5.47080194e-01, -6.75220847e-01,
         1.37227153e-02, 4.96825878e-02, -5.62312914e-01,
         1.09466581e-01, 6.03132575e-01, -2.96695657e-01,
         -6.38165555e-01, -6.05900485e-01, -6.01508174e-02,
         2.14936029e-01, 2.32453208e+00, 7.06358510e-01,
         2.22447092e+00, 8.60057229e-01, -4.15117697e-01,
         -1.61712809e+00, -2.27673666e+00, -4.34904726e-01,
         -1.62324239e+00, 4.48045709e-01, 4.70430778e-01,
         -5.64737343e-01, -1.40765558e+00, 1.19949501e-01,
         2.28388428e+00, -3.35513745e+00, 7.33672887e-01,
         -1.67621107e-01, 4.38908689e-01, 1.11443402e+00,
         -2.59065452e+00, -1.39315541e+00, -8.32371028e-01,
         3.11422291e-02, -1.61132799e+00, -4.84432022e-02,
         -4.11715512e-01, -1.66230288e+00, 5.09891789e-01,
         -9.78537428e-01, 7.27323130e-01, 7.76189356e-01,
         -1.10007446e-01, 2.58812965e-01, 1.13445901e-01,
         -8.53821015e-01, 1.05002528e-01, 7.82956016e-01,
         9.06849638e-01, 6.87469752e-01, -3.81112288e-02,
         -1.03649931e+00, -8.79051897e-01, 8.59547611e-01,
         6.89739014e-01, -8.84752905e-01, -5.01324659e-01,
         1.41592866e-01, -4.64631038e-01, 1.31442590e+00,
         6.10264261e-01, 1.37393187e+00, 1.22939779e+00,
         -2.88723507e-01, 2.72439182e-01, 9.28861628e-01,
         -8.00571068e-01, -6.06420492e-01, -2.89243912e-01,
         -1.40999272e+00, -4.88503424e-01, 1.14552493e-01,
         -8.04342589e-01, -1.73390980e-01, 4.57446313e-01,
         4.46173165e-01, 8.49359050e-02, -1.32696039e+00,
         4.17474655e-01, -4.13901909e-01, 1.94779104e+00,
         -1.14683222e+00, 9.03199227e-01, -8.41775163e-01,
         -2.28948451e+00, 1.41152015e+00, 2.79996546e-01,
         7.26113480e-01, -1.65113635e+00, -7.07981310e-01,
         -1.64011305e+00, 3.28249855e-01, -6.03066907e-01,
         -2.13768271e-01, -7.52212956e-01, 1.51768381e-01,
         -3.38130913e-03, 3.17437312e-01, 4.74313526e-01,
         -3.63678574e-01, -2.04815729e-01, -5.70183214e-01,
         -1.16307198e+00, -4.51352691e-01, 1.87805463e+00,
         -9.84462045e-01, -1.06089995e+00, 1.78792234e-01,
         1.20414190e+00, 7.42684405e-01, 1.60250072e-01,
         -2.49525946e-01, 1.10282074e+00, -3.03869716e-02,
         -2.65310197e+00, 8.03678404e-02, -7.24014076e-01,
         -1.11965929e+00, 1.50054991e-01, 6.70631260e-01,
         -9.19098471e-01, 2.62789325e-01, -1.96046200e+00,
         5.09102738e-01, -2.29135371e-01, -3.52919734e-01,
         1.53115997e+00, -2.82387360e-01, -7.50746472e-01,
         4.32273890e-01, -1.71067948e-01, 1.39891600e+00,
         3.73975175e-01, -4.66445595e-02, -1.28470550e+00,
         1.12953535e+00, 7.54748197e-01, -7.02702952e-02,
         -1.00194646e+00, -6.12820583e-01, -1.37033100e-01,
         -1.07743609e+00, -1.08187959e+00, -9.62350076e-01,
         1.76105062e+00, -1.00107943e+00, 2.39942500e-01,
         -2.33949747e+00, -2.92544582e-01, -1.14312833e-02,
         -1.51159092e-01, -1.63845479e+00]
def faceHX(face_area,RN):

    if RN > 1.5:
        qflux = 3.62
    elif RN < 0.5:
        qflux = 2.58
    else:
        qflux = 1.135*RN+1.9693
    
    q = face_area*qflux

    return q, qflux
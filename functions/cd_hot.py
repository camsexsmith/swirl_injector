def cd_factor(cd_o_c,cd_i_c,RN):

    if RN < 0.6:
        cd_o_k = 0.94159
        cd_i_k = 1.01910
    elif RN > 2:
        cd_o_k = 0.79077
        cd_i_k = 0.93748
    else:
        cd_o_k = -0.1169*RN+1.0224
        cd_i_k = -0.0592*RN+1.0610

    cd_o_h = cd_o_k*cd_o_c
    cd_i_h = cd_i_k*cd_i_c

    return cd_o_h, cd_i_h
import sys

def main():
    swap_txt_in = ''
    for line in sys.stdin:
        for txt in line:
            swap_txt_in += txt
    swap_txt_in = swap_txt_in.rstrip()
    swapping(swap_txt_in)

def swapping(swap_txt_in):
    length_txt = int(len(swap_txt_in))
    if (length_txt % 2) == 0:
        half = ((length_txt//2))
        a_half_txt = swap_txt_in[:half]
        b_half_txt = swap_txt_in[half:]
        swap_txt_out = b_half_txt + a_half_txt
    else:
        half =((length_txt//2))
        a_half_txt = swap_txt_in[:half]
        b_half_txt = swap_txt_in[half:]
        c_txt = swap_txt_in[half]
        swap_txt_out = b_half_txt +c_txt+ a_half_txt

    print('Please give a string to swap: '+swap_txt_out)

main()

' test-swap-o1.stdin '
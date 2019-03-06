def boom_field_map():
    return {
        'Sample in Buffer':                                 'dontCare0',
        'Sample in Window':                                 'dontCare1',
        'TRIGGER':                                          'dontCare2',
        'pardcore_i/system_ila_0/inst/probe0_1':            'valid',
        'pardcore_i/system_ila_0/inst/probe1_1[1:0]':       'commPriv',
        'pardcore_i/system_ila_0/inst/probe2_1[39:0]':      'commPC',
        'pardcore_i/system_ila_0/inst/probe3_1[31:0]':      'commInst',
        'pardcore_i/system_ila_0/inst/probe4_1':            'isFloat',
        'pardcore_i/system_ila_0/inst/probe5_1':            'wbValueValid',
        'pardcore_i/system_ila_0/inst/probe6_1[5:0]':       'wbARFN',
        'pardcore_i/system_ila_0/inst/probe7_1[63:0]':      'wbValue',

        'pardcore_i/system_ila_0/inst/probe8_1[63:0]':      'reg_mbadaddr',
    }


def rocket_field_map():
    return {
        'Sample in Buffer':                                 'dontCare0',
        'Sample in Window':                                 'dontCare1',
        'TRIGGER':                                          'dontCare2',
        'pardcore_i/system_ila_0/inst/probe0_1':            'valid',
        'pardcore_i/system_ila_0/inst/probe1_1[1:0]':       'commPriv',
        'pardcore_i/system_ila_0/inst/probe2_1[39:0]':      'commPC',
        'pardcore_i/system_ila_0/inst/probe3_1[31:0]':      'commInst',
        'pardcore_i/system_ila_0/inst/probe4_1':            'isFloat',
        'pardcore_i/system_ila_0/inst/probe5_1':            'wbValueValid',
        'pardcore_i/system_ila_0/inst/probe6_1[5:0]':       'wbARFN',
        'pardcore_i/system_ila_0/inst/probe7_1[63:0]':      'wbValue',

        'pardcore_i/system_ila_0/inst/probe8_1':            'delayedWbValid',

        'pardcore_i/system_ila_0/inst/probe9_1[63:0]':      'reg_mbadaddr',
    }

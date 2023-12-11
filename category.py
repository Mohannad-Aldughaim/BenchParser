def getSubCat(ssc):
    subcat = ""
    if (ssc == "array-examples" or
            ssc == "array-industry-pattern" or
            ssc == "reducercommutativity" or
            ssc == "array-tiling" or
            ssc == "array-programs" or
            ssc == "array-crafted" or
            ssc == "array-multidimensional" or
            ssc == "array-patterns" or
            ssc == "array-cav19" or
            ssc == "array-lopstr16" or
            ssc == "array-fpi"):
        subcat = "ReachSafety-Arrays"
    elif (ssc == "bitvector" or
          ssc == "bitvector-regression" or
          ssc == "bitvector-loops"):
        subcat = "ReachSafety-BitVectors"
    elif (ssc == "ntdrivers-simplified" or
          ssc == "openssl-simplified" or
          ssc == "locks" or
          ssc == "ntdrivers" or
          ssc == "openssl" or
          ssc == "memory-model" or
          ssc == "unsignedintegeroverflow-sas23" or
          ssc == "longjmp"):
        subcat = "ReachSafety-ControlFlow"
    elif (ssc == "eca-rers2012" or
          ssc == "eca-rers2018" or
          ssc == "psyco" or
          ssc == "eca-programs"):
        subcat = "ReachSafety-ECA"
    elif (ssc == "floats-cdfpl" or
          ssc == "floats-cbmc-regression" or
          ssc == "float-benchs" or
          ssc == "floats-esbmc-regression" or
          ssc == "float-newlib" or
          ssc == "loop-floats-scientific-comp" or
          ssc == "neural-networks"):
        subcat = "ReachSafety-Floats"
    elif (ssc == "heap-manipulation" or
          ssc == "list-properties" or
          ssc == "ldv-regression" or
          ssc == "ddv-machzwd" or
          ssc == "forester-heap" or
          ssc == "list-ext-properties" or
          ssc == "list-ext2-properties" or
          ssc == "ldv-sets" or
          ssc == "list-simple" or
          ssc == "heap-data" or
          ssc == "list-ext3-properties"):
        subcat = "ReachSafety-Heap"
    elif (ssc == "loops" or
          ssc == "loop-acceleration" or
          ssc == "loop-crafted" or
          ssc == "loop-invgen" or
          ssc == "loop-lit" or
          ssc == "loop-new" or
          ssc == "loop-industry-pattern" or
          ssc == "loops-crafted-1" or
          ssc == "loop-invariants" or
          ssc == "loop-simple" or
          ssc == "loop-zilu" or
          ssc == "verifythis/duple" or
          ssc == "verifythis/elimination_m" or
          ssc == "verifythis/l" or
          ssc == "verifythis/prefixsum_it" or
          ssc == "verifythis/tree_del_it" or
          ssc == "verifythis/tree_del_iter_incorre" or
          ssc == "nla-digbench" or
          ssc == "nla-digbench-scaling" or
          ssc == "verifythis"):
        subcat = "ReachSafety-Loops"
    elif ssc == "product-lines":
        subcat = "ReachSafety-ProductLines"
    elif (ssc == "recursive" or
          ssc == "recursive-simple" or
          ssc == "recursive-with-pointer" or
          ssc == "verifythis/prefixsum_r" or
          ssc == "verifythis/tree_del_r" or
          ssc == "verifythis/tree_del_rec_incorre" or
          ssc == "verifythis/tree_m" or
          ssc == "verifythis/tree_max_incorre" or
          ssc == "verifythis/elimination_max_r" or
          ssc == "verifythis/elimination_max_rec_onepoi" or
          ssc == "recursified_loop-crafted" or
          ssc == "recursified_loop-invariants" or
          ssc == "recursified_loop-simple" or
          ssc == "recursified_nla-digbench"):
        subcat = "ReachSafety-Recursive"
    elif (ssc == "systemc" or
          ssc == "seq-mthreaded" or
          ssc == "seq-mthreaded-reduced" or
          ssc == "seq-pthread"):
        subcat = "ReachSafety-Sequentialized"
    elif (ssc == "xcsp"):
        subcat = "ReachSafety-XCSP"
    elif (ssc == "combinations"):
        subcat = "ReachSafety-Combinations"
    elif (ssc == "pthread" or
          ssc == "pthread-atomic" or
          ssc == "pthread-ext" or
          ssc == "pthread-wmm" or
          ssc == "pthread-lit" or
          ssc == "ldv-races" or
          ssc == "ldv-linux-3.14-races" or
          ssc == "pthread-complex" or
          ssc == "pthread-driver-races" or
          ssc == "pthread-C-DAC" or
          ssc == "pthread-divine" or
          ssc == "pthread-nondet" or
          ssc == "goblint-regression" or
          ssc == "weaver" or
          ssc == "pthread-deagle"):
        subcat = "ConcurrencySafety-Main"
    elif (ssc == "array-memsafety" or
          ssc == "array-examples" or
          ssc == "array-memsafety-realloc" or
          ssc == "termination-crafted/Array" or
          ssc == "termination-crafted/LexIndexValu" or
          ssc == "termination-crafted/NonTermination3" or
          ssc == "verifythis/duple" or
          ssc == "verifythis/elimination_m" or
          ssc == "verifythis/l" or
          ssc == "verifythis/prefixsum_it" or
          ssc == "verifythis/elimination_max_r" or
          ssc == "verifythis/elimination_max_rec_onepoi"):
        subcat = "MemSafety-Arrays"
    elif (ssc == "memsafety" or
          ssc == "memsafety-ext" or
          ssc == "memsafety-ext2" or
          ssc == "list-ext-properties" or
          ssc == "memory-alloca" or
          ssc == "ldv-memsafety" or
          ssc == "ldv-memsafety-bitfields"):
        subcat = "MemSafety-Heap"
    elif (ssc == "heap-manipulation" or
          ssc == "forester-heap" or
          ssc == "list-properties" or
          ssc == "ddv-machzwd" or
          ssc == "list-simple" or
          ssc == "list-ext3-properties"):
        subcat = "MemSafety-LinkedLists"
    elif (ssc == "loops" or
          ssc == "loop-acceleration" or
          ssc == "ntdrivers" or
          ssc == "ntdrivers-simplified" or
          ssc == "locks" or
          ssc == "memsafety-ext3" or
          ssc == "pthread-memsafety" or
          ssc == "memsafety-bftpd" or
          ssc == "termination-crafted/4BitCounterPoint" or
          ssc == "termination-crafted/SyntaxSupportPointe"):
        subcat = "MemSafety-Other"
    elif (ssc == "aws-c-common"):
        subcat = "SoftwareSystems-AWS-C-Common-ReachSafety"
    elif (ssc == "busybox-1.22.0"):
        subcat = "SoftwareSystems-BusyBox-ReachSafety"
    elif (ssc == "busybox-1.22.0"):
        subcat = "SoftwareSystems-BusyBox-NoOverflows"
    elif (ssc == "ldv-linux-3.0" or
          ssc == "ldv-linux-3.4-simple" or
          ssc == "ldv-linux-3.7.3" or
          ssc == "ldv-commit-tester" or
          ssc == "ldv-consumption" or
          ssc == "ldv-linux-3.12-rc1" or
          ssc == "ldv-linux-3.16-rc1" or
          ssc == "ldv-validator-v0.6" or
          ssc == "ldv-validator-v0.8" or
          ssc == "ldv-linux-4.2-rc1" or
          ssc == "ldv-linux-3.14" or
          ssc == "ldv-challenges" or
          ssc == "ldv-linux-4.0-rc1-mav"):
        subcat = "SoftwareSystems-DeviceDriversLinux64-ReachSafety"
    elif (ssc == "uthash-2.0.2"):
        subcat = "SoftwareSystems-uthash-ReachSafety"
    elif (ssc == "hardware-verification-array" or ssc == "hardware-verification-bv"):
        subcat = "ReachSafety-Hardware"
    elif(ssc == "fuzzle-programs"):
        subcat = "ReachSafety-Fuzzle"
    elif ():
        subcat = ""

    return subcat


def getCat(subcat):
    cat = ""
    if subcat.startswith("ReachSafety"):
        cat = "ReachSafety"
    if subcat.startswith("ConcurrencySafety"):
        cat = "ConcurrencySafety"
    if subcat.startswith("MemSafety"):
        cat = "MemSafety"
    if subcat.startswith("SoftwareSystems"):
        cat = "SoftwareSystems"
    return cat


def getScore(CTRL, result):
    if CTRL:
        if result.startswith("false"):
            return -16
        elif result.startswith("true"):
            return 2
    elif CTRL:
        if result.startswith("false"):
            return 1
        elif result.startswith("true"):
            return -32
    return 0

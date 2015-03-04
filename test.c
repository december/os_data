#include "stdlib.h"

struct gatedesc {
    unsigned gd_off_15_0 : 16;        // low 16 bits of offset in segment
    unsigned gd_ss : 16;            // segment selector
    unsigned gd_args : 5;            // # args, 0 for interrupt/trap gates
    unsigned gd_rsv1 : 3;            // reserved(should be zero I guess)
    unsigned gd_type : 4;            // type(STS_{TG,IG32,TG32})
    unsigned gd_s : 1;                // must be 0 (system)
    unsigned gd_dpl : 2;            // descriptor(meaning new) privilege level
    unsigned gd_p : 1;                // Present
    unsigned gd_off_31_16 : 16;        // high bits of offset in segment
};

typedef struct gatedesc gatedesc;
typedef unsigned int uint32_t;

#define STS_IG32    0xE     // 32-bit Interrupt Gate
#define STS_TG32    0xF     // 32-bit Trap Gate

#define SETGATE(gate, istrap, sel, off, dpl) {            \
    ((gatedesc*)(&gate))->gd_off_15_0 = (uint32_t)(off) & 0xffff;        \
    ((gatedesc*)(&gate))->gd_ss = (sel);                                \
    ((gatedesc*)(&gate))->gd_args = 0;                                    \
    ((gatedesc*)(&gate))->gd_rsv1 = 0;                                    \
    ((gatedesc*)(&gate))->gd_type = (istrap) ? STS_TG32 : STS_IG32;    \
    ((gatedesc*)(&gate))->gd_s = 0;                                    \
    ((gatedesc*)(&gate))->gd_dpl = (dpl);                                \
    ((gatedesc*)(&gate))->gd_p = 1;                                    \
    ((gatedesc*)(&gate))->gd_off_31_16 = (uint32_t)(off) >> 16;        \
}

int main()
{
	unsigned intr;
	intr=8;
	SETGATE(intr, 0,1,2,3);
	printf("%d", intr);
	return 0;
}

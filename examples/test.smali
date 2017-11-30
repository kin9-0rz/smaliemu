
# direct methods
.method static constructor <clinit>()V
    .registers 12

    const/16 v0, 0x8

    new-array v3, v0, [Ljava/lang/String;

    const/4 v2, 0x0

    const-string v1, "]2e\u000f"

    const/4 v0, -0x1

    move-object v4, v3

    :goto_9
    invoke-virtual {v1}, Ljava/lang/String;->toCharArray()[C

    move-result-object v1

    array-length v5, v1

    const/4 v6, 0x0

    const/4 v7, 0x1

    if-gt v5, v7, :cond_2e

    :cond_12
    move-object v7, v1

    move v8, v6

    move v11, v5

    move-object v5, v1

    move v1, v11

    :goto_17
    aget-char v10, v5, v6

    rem-int/lit8 v9, v8, 0x5

    packed-switch v9, :pswitch_data_84

    const/16 v9, 0x72

    :goto_20
    xor-int/2addr v9, v10

    int-to-char v9, v9

    aput-char v9, v5, v6

    add-int/lit8 v6, v8, 0x1

    if-nez v1, :cond_2c

    move-object v5, v7

    move v8, v6

    move v6, v1

    goto :goto_17

    :cond_2c
    move v5, v1

    move-object v1, v7

    :cond_2e
    if-gt v5, v6, :cond_12

    new-instance v5, Ljava/lang/String;

    invoke-direct {v5, v1}, Ljava/lang/String;-><init>([C)V

    invoke-virtual {v5}, Ljava/lang/String;->intern()Ljava/lang/String;

    move-result-object v1

    packed-switch v0, :pswitch_data_90

    aput-object v1, v3, v2

    const/4 v2, 0x1

    const-string v1, "\u0019l5\u0019\u001d\u0011f\u007f\u0002\u001c\u000cg?\u001f\\\u0019a%\u0002\u001d\u0016,\u001c*;6"

    const/4 v0, 0x0

    move-object v3, v4

    goto :goto_9

    :pswitch_44
    aput-object v1, v3, v2

    const/4 v2, 0x2

    const-string v1, "\u0019l5\u0019\u001d\u0011f\u007f\u0002\u001c\u000cg?\u001f\\\u001bc%\u000e\u0015\u0017p(E:7O\u0014"

    const/4 v0, 0x1

    move-object v3, v4

    goto :goto_9

    :pswitch_4c
    aput-object v1, v3, v2

    const/4 v2, 0x3

    const-string v1, "\u0013g(\u000c\u0007\u0019p5"

    const/4 v0, 0x2

    move-object v3, v4

    goto :goto_9

    :pswitch_54
    aput-object v1, v3, v2

    const/4 v2, 0x4

    const-string v1, "\u001cg\'\u0002\u0011\u001d]!\u0004\u001e\u0011a("

    const/4 v0, 0x3

    move-object v3, v4

    goto :goto_9

    :pswitch_5c
    aput-object v1, v3, v2

    const/4 v2, 0x5

    const-string v1, "\u0013g(\u000c\u0007\u0019p5"

    const/4 v0, 0x4

    move-object v3, v4

    goto :goto_9

    :pswitch_64
    aput-object v1, v3, v2

    const/4 v2, 0x6

    const-string v1, "\']\"\u0000\u001e\u0019q\"\u000e-\u0011l8\u001f"

    const/4 v0, 0x5

    move-object v3, v4

    goto :goto_9

    :pswitch_6c
    aput-object v1, v3, v2

    const/4 v2, 0x7

    const-string v1, "\']\"\u0000\u001e\u0019q\"\u000e-\u0011l8\u001f"

    const/4 v0, 0x6

    move-object v3, v4

    goto :goto_9

    :pswitch_74
    aput-object v1, v3, v2

    sput-object v4, Lowd/qusutsqfdo/mbpepvxhxly/IlllIllIlIIlllllIlllllIIllIllIIIIllIlllllLllllLIILLIIIIl;->a:[Ljava/lang/String;

    return-void

    :pswitch_79
    const/16 v9, 0x78

    goto :goto_20

    :pswitch_7c
    const/4 v9, 0x2

    goto :goto_20

    :pswitch_7e
    const/16 v9, 0x51

    goto :goto_20

    :pswitch_81
    const/16 v9, 0x6b

    goto :goto_20

    :pswitch_data_84
    .packed-switch 0x0
        :pswitch_79
        :pswitch_7c
        :pswitch_7e
        :pswitch_81
    .end packed-switch

    :pswitch_data_90
    .packed-switch 0x0
        :pswitch_44
        :pswitch_4c
        :pswitch_54
        :pswitch_5c
        :pswitch_64
        :pswitch_6c
        :pswitch_74
    .end packed-switch
.end method

.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo(I)I
.var 0 is n I from Label0 to Label1
Label0:
Label2:
	iload_0
	iconst_2
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	iload_0
	bipush 100
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	iconst_1
	ineg
	ireturn
Label15:
	goto Label11
Label10:
Label16:
	iconst_0
	ireturn
Label17:
Label11:
Label9:
	goto Label5
Label4:
Label18:
	iconst_0
	ireturn
Label19:
Label5:
Label3:
	nop
Label1:
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_1
	invokestatic MiniGoClass/foo(I)I
	invokestatic io/putInt(I)V
Label3:
	nop
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

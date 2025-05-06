.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static factorial(I)I
.var 0 is n I from Label0 to Label1
Label0:
Label2:
	iload_0
	iconst_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	iconst_1
	ineg
	ireturn
Label9:
	goto Label5
Label4:
Label10:
	iconst_1
	ireturn
Label11:
Label5:
Label3:
	nop
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	bipush 102
	ineg
	invokestatic MiniGoClass/factorial(I)I
	invokestatic io/putIntLn(I)V
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

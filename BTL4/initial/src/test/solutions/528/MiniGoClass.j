.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is c I from Label2 to Label3
	iconst_2
	istore_1
.var 2 is d I from Label2 to Label3
	iconst_5
	istore_2
.var 3 is b Z from Label2 to Label3
	iload_1
	iload_2
	if_icmpne Label4
	iload_1
	iload_2
	if_icmpge Label4
	iload_1
	iload_2
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore_3
	iload_3
	invokestatic io/putBool(Z)V
Label3:
	nop
Label1:
	return
.limit stack 8
.limit locals 4
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

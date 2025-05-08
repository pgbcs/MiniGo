.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a F from Label2 to Label3
	ldc 5.5
	fstore_1
.var 2 is b F from Label2 to Label3
	ldc 10.0
	fstore_2
	fload_1
	fload_2
	fcmpl
	ifle Label6
	iconst_0
	iconst_0
	idiv
	iconst_0
	if_icmple Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
Label8:
	fload_1
	fload_2
	fadd
	invokestatic io/putFloatLn(F)V
Label9:
	goto Label5
Label4:
Label10:
	fload_1
	fload_2
	fsub
	invokestatic io/putFloatLn(F)V
Label11:
Label5:
Label3:
	nop
Label1:
	return
.limit stack 3
.limit locals 3
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

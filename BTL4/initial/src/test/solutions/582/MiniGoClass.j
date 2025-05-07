.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static add(FF)F
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
Label2:
	fload_0
	fload_1
	fadd
	freturn
Label3:
	nop
Label1:
.limit stack 2
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a F from Label2 to Label3
	ldc 5.5
	fstore_1
.var 2 is b F from Label2 to Label3
	ldc 10.5
	fstore_2
.var 3 is c F from Label2 to Label3
	fload_1
	fload_2
	invokestatic MiniGoClass/add(FF)F
	fstore_3
	fload_3
	invokestatic io/putFloatLn(F)V
	ldc 3.5
	ldc 4.5
	invokestatic MiniGoClass/add(FF)F
	invokestatic io/putFloatLn(F)V
	ldc 1.5
	ldc 2.5
	invokestatic MiniGoClass/add(FF)F
	ldc 3.5
	ldc 4.5
	invokestatic MiniGoClass/add(FF)F
	fadd
	invokestatic io/putFloatLn(F)V
	ldc 1.5
	ldc 2.5
	invokestatic MiniGoClass/add(FF)F
	ldc 3.5
	ldc 4.5
	invokestatic MiniGoClass/add(FF)F
	invokestatic MiniGoClass/add(FF)F
	invokestatic io/putFloatLn(F)V
Label3:
	nop
Label1:
	return
.limit stack 3
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

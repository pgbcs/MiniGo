.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is b LCrocodilo; from Label2 to Label3
	new Crocodilo
	dup
	invokespecial Crocodilo/<init>()V
	dup
	iconst_4
	putfield Crocodilo/value I
	astore_1
	aload_1
	getfield Crocodilo/value I
	invokestatic io/putInt(I)V
Label3:
	nop
Label1:
	return
.limit stack 3
.limit locals 2
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

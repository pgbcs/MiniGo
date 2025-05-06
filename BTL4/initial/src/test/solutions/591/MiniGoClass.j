.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is people LPrinter; from Label2 to Label3
	aconst_null
	astore_1
	new Pearson
	dup
	invokespecial Pearson/<init>()V
	dup
	ldc "Bob"
	putfield Pearson/name Ljava/lang/String;
	astore_1
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

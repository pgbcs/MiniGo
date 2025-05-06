.source Pearson.java
.class public Pearson
.super java.lang.Object
.implements Printer
.field name Ljava/lang/String;

.method public <init>()V
.var 0 is this LPearson; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aconst_null
	putfield Pearson/name Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public say()V
.var 0 is this LPearson; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield Pearson/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
	nop
Label1:
	return
.limit stack 1
.limit locals 1
.end method

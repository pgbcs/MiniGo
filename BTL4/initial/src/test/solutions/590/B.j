.source B.java
.class public B
.super java.lang.Object
.implements Printable
.field age I
.field name Ljava/lang/String;

.method public <init>()V
.var 0 is this LB; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield B/age I
	aload_0
	aconst_null
	putfield B/name Ljava/lang/String;
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public print()V
.var 0 is this LB; from Label0 to Label1
Label0:
Label2:
	aload_0
	getfield B/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield B/age I
	invokestatic io/putIntLn(I)V
Label3:
	nop
Label1:
	return
.limit stack 1
.limit locals 1
.end method

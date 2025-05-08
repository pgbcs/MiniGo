.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is people [LPrinter; from Label2 to Label3
	aconst_null
	astore_1
	iconst_3
	anewarray Person
	dup
	iconst_0
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Anna"
	putfield Person/name Ljava/lang/String;
	aastore
	dup
	iconst_1
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Ben"
	putfield Person/name Ljava/lang/String;
	aastore
	dup
	iconst_2
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Cara"
	putfield Person/name Ljava/lang/String;
	aastore
	astore_1
.var 2 is i I from Label2 to Label3
	iconst_0
	istore_2
Label6:
	iload_2
	iconst_3
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label5
Label9:
.var 3 is p LPrinter; from Label9 to Label10
	aload_1
	iload_2
	aaload
	astore_3
	aload_3
	invokeinterface Printer/print()V 1
Label10:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label6
Label5:
Label3:
	nop
Label1:
	return
.limit stack 6
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

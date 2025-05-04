.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a Z from Label2 to Label3
	iconst_1
	istore_1
.var 2 is b Z from Label2 to Label3
	iconst_0
	istore_2
.var 3 is c Z from Label2 to Label3
	iconst_1
	istore_3
.var 4 is d Z from Label2 to Label3
	iconst_1
	istore 4
.var 5 is e Z from Label2 to Label3
	iconst_1
	istore 5
.var 6 is f Z from Label2 to Label3
	iload_1
	ifgt Label6
	iload_2
	ifle Label8
	iload_3
	ifle Label8
	goto Label6
Label8:
	goto Label4
Label6:
	iload 4
	ifle Label4
	iload 5
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	istore 6
	iload 6
	invokestatic io/putBool(Z)V
Label3:
Label1:
	return
.limit stack 2
.limit locals 7
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

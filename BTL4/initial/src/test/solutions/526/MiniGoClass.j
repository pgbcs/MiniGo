.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a Z = 1
.field static b I = 1

.method public static B(I)I
.var 0 is c I from Label0 to Label1
Label0:
Label2:
	iconst_1
	ireturn
Label3:
	nop
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/b I
	invokestatic MiniGoClass/B(I)I
	ineg
	invokestatic io/putIntLn(I)V
	getstatic MiniGoClass/a Z
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
Label3:
	nop
Label1:
	return
.limit stack 2
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

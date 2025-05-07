.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a I = 5
.field static c F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is b F from Label2 to Label3
	getstatic MiniGoClass/a I
	i2f
	fstore_1
	fload_1
	invokestatic io/putFloat(F)V
	getstatic MiniGoClass/c F
	invokestatic io/putFloat(F)V
Label3:
	nop
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static <clinit>()V
Label0:
	getstatic MiniGoClass/a I
	i2f
	putstatic MiniGoClass/c F
Label1:
	return
.limit stack 1
.limit locals 0
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

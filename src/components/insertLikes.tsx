/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";
import { handleInsertLike } from "./insert-likes";
import { usePalettes } from "./UsernameContext";
import { usePathname } from "next/navigation";
import { useState } from "react"; // Import useState

export default function InsertLikes({
  likes_count,
  color1,
  color2,
  color3,
  color4,
}: any) {
  const { addPalette, deletePalette } = usePalettes();
  const [currentLikesCount, setCurrentLikesCount] = useState(likes_count); // Initialize state for likes count

  const paletteId = `${color1}${color2}${color3}${color4}`; // حفظ القيمة المحسوبة لإستخدامها لاحقًا

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (paletteId) {
      await handleInsertLike(paletteId); // إرسال معرف اللوحة كـ id بدلاً من إضافة الألوان
    }
  };

  const handleAddPalette = () => {
    const newPalette = { color1, color2, color3, color4, id: paletteId };
    addPalette(newPalette);
    setCurrentLikesCount(currentLikesCount + 1); // Increase likes count only when adding a palette
  };

  const handleDeletePalette = () => {
    deletePalette(paletteId);
    setCurrentLikesCount(currentLikesCount - 1); // Decrease likes count when deleting a palette
  };

  const { palettes } = usePalettes();
  const isVerified = palettes.some((palette: any) => palette.id === paletteId); // استخدام id المحسوب للتأكد من وجود اللوحة

  const Pathname = usePathname();

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <button
          type="submit"
          onClick={
            isVerified ? handleDeletePalette : handleAddPalette // Use handleDeletePalette for deletion
          }
        >
          <div
            className={`flex items-center justify-center border-[1px] border-stone-200/80 p-2 px-3 gap-2 rounded-xl ${
              isVerified ? "bg-stone-200/80" : ""
            }`}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill={isVerified ? "red" : "none"}
              stroke={isVerified ? "red" : "currentColor"}
              viewBox="0 0 24 24"
              strokeWidth={0.6}
              className="size-6"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12Z"
              />
            </svg>
            {Pathname !== `/collection` && (
              <span className="text-sm font-extralight">{currentLikesCount}</span>
            )}
          </div>
        </button>
      </form>
    </div>
  );
}

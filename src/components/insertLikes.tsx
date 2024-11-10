/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";
import { handleInsertLike } from "./insert-likes";
import { usePalettes } from "./UsernameContext";
import { usePathname } from "next/navigation";

export default function InsertLikes({
  id,
  likes_count,
  color1,
  color2,
  color3,
  color4,
}: any) {
  const { addPalette, deletePalette } = usePalettes();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (id) {
      await handleInsertLike(id);
    }
  };

  const handleAddPalette = () => {
    const newPalette = {
      color1,
      color2,
      color3,
      color4,
      id,
    };

    addPalette(newPalette);
  };

  const { palettes } = usePalettes();
  const isVerified = palettes.some((palette: any) => palette.id === id);
  const Pathname = usePathname();

  return (
    <div>
      <form
        onSubmit={handleSubmit}
        onClick={isVerified ? () => deletePalette(id) : handleAddPalette}
      >
        <button type="submit">
          <div
            className={`flex items-center justify-center border-[1px] border-stone-200/80 p-2 px-3 gap-2 rounded-xl  ${
              isVerified && "bg-stone-200/80"
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
              <span className="text-sm font-extralight">{likes_count}</span>
            )}
          </div>
        </button>
      </form>
    </div>
  );
}
